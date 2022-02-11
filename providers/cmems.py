"""Access to CMEMS[https://marine.copernicus.eu/] datasets, 
you will need to be registered and use your credentials"""

import os
import xarray as xr
from getpass import getpass
from datetime import datetime
import numpy as np

# form providers.cmems import CmemsOpendap

class CmemsOpendap:
    def __init__(
        self,
        dataset_id: str,
        username: str = None,
        password: str = None,
    ):

        if username is None:
            username = getpass("Enter your username: ")
        if password is None:
            password = getpass("Enter your password: ")

        self.username = username
        self.password = password

        # Connect to datastore
        data_store = copernicusmarine_datastore(dataset_id, username, password)
        self.ds = xr.open_dataset(data_store)
        print(f"\033[1;32m'{username}' is successfully connected to '{dataset_id}'. xarray-dataset is in 'your_instance.ds'\033[0;0m")


    def crop(
        self,
        variables: list = None,
        times: slice(datetime) = None,
        longitudes: slice(float) = None,
        latitudes: slice(float) = None,
        depths: slice(float) = None,
        method: str = "neareast_outside",
    ):
        # -----------------------------------------------------------------------
        # BUG - Repeted times! waiting response from cmems-service!
        # WORKARROUND - Check there are no repeted times, it there are drop them!
        if len(np.unique(self.ds.time.values)) != len(self.ds.time):
            print("Repeated times founded! --> report to Elena: edimedio@mercator-ocean.eu")
            _, index = np.unique(self.ds["time"], return_index=True)
            self.ds = self.ds.isel(time=index)
        # -----------------------------------------------------------------------

        # Modify coordinates to make the selection based on the method desired 
        if method == "neareast_outside":
            # Calculate your domain and add 1 maximum dt, dx, dy as an outside buffer
            if isinstance(times, slice):
                times = slice(
                    times.start
                    - np.diff(self.ds["time"].values)
                    .max()
                    .astype("timedelta64[s]")
                    .item(),
                    times.stop
                    + np.diff(self.ds["time"].values)
                    .max()
                    .astype("timedelta64[s]")
                    .item(),
                )

            if isinstance(longitudes, slice):
                longitudes = slice(
                    longitudes.start - np.diff(self.ds["longitude"].values).max(),
                    longitudes.stop + np.diff(self.ds["longitude"].values).max(),
                )

            if isinstance(latitudes, slice):
                latitudes = slice(
                    latitudes.start - np.diff(self.ds["latitude"].values).max(),
                    latitudes.stop + np.diff(self.ds["latitude"].values).max(),
                )

        # Make the selection of coordinates
        if times is not None:
            if isinstance(times, slice):
                self.ds = self.ds.sel(time=times)
            else:
                self.ds = self.ds.sel(time=times, method="nearest")

        if longitudes is not None:
            if isinstance(longitudes, slice):
                self.ds = self.ds.sel(longitude=longitudes)
            else:
                self.ds = self.ds.sel(longitude=longitudes, method="nearest")

        if latitudes is not None:
            if isinstance(latitudes, slice):
                self.ds = self.ds.sel(latitude=latitudes)
            else:
                self.ds = self.ds.sel(latitude=latitudes, method="nearest")

        if depths is not None:
            if isinstance(depths, slice):
                self.ds = self.ds.sel(detph=depths)
            else:
                self.ds = self.ds.sel(detph=depths, method="nearest")

        # Make the selection of variables
        if variables is not None:
            self.ds = self.ds.get(variables)
        
        self.ds.load()

    def to_netcdf(self, output_path: str, netcdf_format: str = None):
        output_path = os.path.abspath(output_path)
        try:
            self.ds.to_netcdf(output_path, format=netcdf_format)

        except:
            output_dir = os.path.dirname(output_path)
            filename, file_ext = os.path.splitext(os.path.basename(output_path))

            print("Too big to be saved in one file! Spliting files by days...")
            date, datasets = zip(*self.ds.groupby("time.date"))
            paths = [
                f"{output_dir}/{filename}_{d}{file_ext}".replace("-", "") for d in date
            ]
            xr.save_mfdataset(datasets, paths, format=netcdf_format)

def copernicusmarine_datastore(dataset, username, password):
    __author__ = "Copernicus Marine User Support Team"
    __copyright__ = "(C) 2021 E.U. Copernicus Marine Service Information"
    __credits__ = ["E.U. Copernicus Marine Service Information"]
    __license__ = "MIT License - You must cite this source"
    __version__ = "202104"
    __maintainer__ = "D. Bazin, E. DiMedio, C. Giordan"
    __email__ = "servicedesk dot cmems at mercator hyphen ocean dot eu"

    from pydap.client import open_url
    from pydap.cas.get_cookies import setup_session

    cas_url = "https://cmems-cas.cls.fr/cas/login"
    session = setup_session(cas_url, username, password)
    session.cookies.set("CASTGC", session.cookies.get_dict()["CASTGC"])
    database = ["my", "nrt"]
    url = f"https://{database[0]}.cmems-du.eu/thredds/dodsC/{dataset}"

    try:
        data_store = xr.backends.PydapDataStore(open_url(url, session=session))
    except:
        url = f"https://{database[1]}.cmems-du.eu/thredds/dodsC/{dataset}"
        data_store = xr.backends.PydapDataStore(open_url(url, session=session))
    return data_store


if __name__ == "__main__":

    # cmems_mod_glo_phy_anfc_merged-uv_PT1H-i
    dataset_id = input("Enter dataset-id form CMEMS-Opendap service: ")
    data = CmemsOpendap(dataset_id, "garagon", "wrHZeS5V")
    print(data.ds)

    
