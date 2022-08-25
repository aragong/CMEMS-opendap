"""Access bathymetries providers"""

import xarray as xr

# TODO - Add GEBCO and EMODnet from IHCantabria

import os


GEBCO_URL = os.environ.get("GEBCO_OPENDAP_URL")
EMODNET_URL = os.environ.get("EMODNET_OPENDAP_URL")

class BathymetryOpendap:

    def __init__(self, dataset:str):
        if dataset.lower() == "gebco":
            self.ds = xr.open_dataset(GEBCO_URL)
        elif dataset.lower() == "emodnet":
            self.ds = xr.open_dataset(EMODNET_URL)







