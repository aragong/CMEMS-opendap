"""Access to NOAA NOMADS[https://nomads.ncep.noaa.gov/] datasets"""

import xarray as xr
import pandas as pd
from datetime import datetime, timedelta

from metoceanproviders.exceptions import DatasetNameError

# gfs_0p25_1hr_example = "http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20220225/gfs_0p25_1hr_00z"
# gfs_0p25_example = "http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs20220216/gfs_0p25_00z"


class NoaaOpendap:
    # TODO - refactor based on dataset dictionary
    datasets = [
        {
            "name": "gfs_0p25",
            "varaibles": ["ugrd10m", "vgrd10m", "vissfc"],
            "spatial_resolution": 0.25,
            "temporal_resolution": "3-hourly",
        },
        {
            "name": "gfs_0p25_1hr",
            "varaibles": ["ugrd10m", "vgrd10m", "vissfc"],
            "spatial_resolution": 0.25,
            "temporal_resolution": "hourly",
        },
    ]

    def __init__(self, dataset: str, extra_variables: list = []):
        """Access NOAA NOMADS Opendap service. Datasets:\n
        NOAA GFS 0.25º: winds@10m and visibility by default. https://nomads.ncep.noaa.gov/dods/gfs_0p25 \n
        NOAA GFS 0.25º (1hr): winds@10m by default. https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr \n

        Args:
            dataset (str): choose dataset name 'gfs_0p25_1hr' or 'gfs_0p25'
            extra_varaibles (list): list of extra variable names to be downloaded accessed.

        Raises:
            DatasetNameError: Custom error for invalid dataset
        """
        self.dataset = dataset
        urls = self._get_urls(dataset)

        self.ds = None
        while not isinstance(self.ds, xr.Dataset):
            try:
                # print(f"Triying to connect to '{urls[0]}'...\n")
                self.ds = xr.open_dataset(urls[0])
                if dataset == "gfs_0p25_1hr":
                    self.ds = self.ds.get(
                        ["ugrd10m", "vgrd10m", "vissfc"] + extra_variables
                    )
                elif dataset == "gfs_0p25":
                    self.ds = self.ds.get(
                        ["ugrd10m", "vgrd10m", "vissfc"] + extra_variables
                    )
                print(f"\033[1;32mSuccessfully connected to '{urls[0]}'\033[0;0m\n")
            except:
                urls = urls[1:]

        self.ds["time"] = self.ds.time.dt.round("min")

    def _get_urls(self, dataset, last_timedelta=timedelta(days=1)):
        t0 = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        days = pd.date_range(start=t0 - last_timedelta, end=t0, freq="D")
        urls = []
        for day in days:
            day = day.strftime("%Y%m%d")
            if dataset == "gfs_0p25_1hr":
                urls.extend(
                    [
                        f"http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs{day}/gfs_0p25_1hr_{update}z"
                        for update in ["00", "06", "12", "18"]
                    ]
                )
            elif dataset == "gfs_0p25":
                urls.extend(
                    [
                        f"http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs{day}/gfs_0p25_{update}z"
                        for update in ["00", "06", "12", "18"]
                    ]
                )
            else:
                raise DatasetNameError(
                    "\n\033[1;31mDataset names allowed are 'gfs_0p25_1hr' or 'gfs_0p25'\033[0;0m\n"
                )
        urls.sort(reverse=True)
        return urls


if __name__ == "__main__":
    data = NoaaOpendap(dataset="gfs_0p25_1hr")
    print(NoaaOpendap.datasets)
    print(data.ds)
