import os
import unittest

import pandas as pd
import xarray as xr
from datetime import datetime, timedelta

from metocean_providers.cmems import CmemsOpendap


class TestCmems(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def setUp(self) -> None:
        self.data = CmemsOpendap(
            "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i", "garagon", "wrHZeS5V"
        )

    def tearDown(self) -> None:
        pass

    def test_cmems_opendap(self):
        self.assertIsInstance(self.data.ds, xr.Dataset)

    def test_crop(self):

        # 5-day forecast
        t0 = datetime.utcnow()
        times = slice(t0, t0 + timedelta(days=5))

        # Balearic Islands
        longitudes = slice(-1, 6)
        latitudes = slice(37, 42)

        self.data.crop(None, times, longitudes, latitudes)

        self.assertTrue(
            pd.Timestamp(self.data.ds.time.values.min()).to_pydatetime() <= times.start
        )
        self.assertTrue(
            pd.Timestamp(self.data.ds.time.values.max()).to_pydatetime() >= times.stop
        )

        self.assertTrue(self.data.ds.longitude.values.min() <= longitudes.start)
        self.assertTrue(self.data.ds.longitude.values.max() >= longitudes.stop)

        self.assertTrue(self.data.ds.latitude.values.min() <= latitudes.start)
        self.assertTrue(self.data.ds.latitude.values.max() >= latitudes.stop)

    def test_to_netcdf(self):
        # 5-day forecast
        t0 = datetime.utcnow()
        times = slice(t0, t0 + timedelta(days=5))

        self.data.crop(None, times, None, None)

        if not os.path.exists("tmp"):
            os.mkdir("tmp")
        path = "tmp/test_save_netcdf.nc"
        self.data.to_netcdf(path)
