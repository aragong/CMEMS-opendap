import unittest

import xarray as xr
from metocean_providers.cmems import CmemsOpendap


class TestForcings(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_cmems_opendap(self):
        data = CmemsOpendap(
            "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i", "garagon", "wrHZeS5V"
        )
        self.assertIsInstance(data.ds, xr.Dataset)
