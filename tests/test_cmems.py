import os
from datetime import datetime, timedelta

import pandas as pd
import pytest
import xarray as xr
from metoceanproviders import config as cfg
from metoceanproviders.cmems import (CredentialsError, Opendap,
                                     _copernicusmarine_datastore)


class TestLogin:
    def test_login_fail(self):
        with pytest.raises(CredentialsError) as e_info:
            _copernicusmarine_datastore("cmems_mod_glo_phy_anfc_merged-uv_PT1H-i", "fakeuser", "fakepass")
    
    def test_login_none(self):
        with pytest.raises(CredentialsError) as e_info:
            _copernicusmarine_datastore("cmems_mod_glo_phy_anfc_merged-uv_PT1H-i", None, None)

class TestOpendap:
    credentials = pytest.mark.skipif(
        None in [cfg.CMEMS_USERNAME, cfg.CMEMS_PASSWORD], 
        reason="\n\033[1;31m'CMEMS_USERNAME' and 'CMEMS_PASSWORD' environment variables are not defined. See Installation in README.md.\033[0;0m\n"
    )

    @pytest.fixture()
    def data(self):
        return Opendap("cmems_mod_glo_phy_anfc_merged-uv_PT1H-i")

    @credentials
    def test_opendap(self, data):
        assert isinstance(data.ds, xr.Dataset)

    @credentials
    def test_crop(self, data):
            # 5-day forecast
            t0 = datetime.utcnow()
            times = slice(t0, t0 + timedelta(days=1))
            # Balearic Islands
            longitudes = slice(-1, 6)
            latitudes = slice(37, 42)
            data.crop(None, times, longitudes, latitudes)
            assert pd.Timestamp(data.ds.time.values.min()).to_pydatetime() <= times.start
            assert pd.Timestamp(data.ds.time.values.max()).to_pydatetime() >= times.stop
            assert data.ds.longitude.values.min() <= longitudes.start
            assert data.ds.longitude.values.max() >= longitudes.stop
            assert data.ds.latitude.values.min() <= latitudes.start
            assert data.ds.latitude.values.max() >= latitudes.stop


    @credentials
    @pytest.mark.slow
    def test_download(self, tmpdir, data):
        if not os.path.exists(tmpdir):
            os.makedirs(tmpdir.dirname)
        path = os.path.join(tmpdir, "test_netcdf.nc")
        t0 = datetime.utcnow()
        times = slice(t0, t0 + timedelta(days=1))
        data.crop(None, times, slice(0,90), slice(0,90))
        data.to_netcdf(path)
        path = os.path.join(tmpdir, "test_netcdf.nc")
        ds = xr.open_dataset(path)
        assert ds == data.ds

