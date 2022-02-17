import os
from datetime import datetime, timedelta

import pandas as pd
import pytest
import xarray as xr
from metoceanproviders import config as cfg
from metoceanproviders.cmems import (
    CredentialsError,
    Opendap,
    _copernicusmarine_datastore,
)


class TestLogin:
    def test_login_fail(self):
        with pytest.raises(CredentialsError) as e_info:
            _copernicusmarine_datastore(
                "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i", "fakeuser", "fakepass"
            )

    def test_login_none(self):
        with pytest.raises(CredentialsError) as e_info:
            _copernicusmarine_datastore(
                "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i", None, None
            )


credentials = pytest.mark.skipif(
    None in [cfg.CMEMS_USERNAME, cfg.CMEMS_PASSWORD],
    reason="\n\033[1;31m'CMEMS_USERNAME' and 'CMEMS_PASSWORD' environment variables are not defined. See Installation in README.md.\033[0;0m\n",
)


class TestOpendap:
    @pytest.fixture(scope="class")
    def times(self):
        t0 = datetime.utcnow()
        return slice(t0, t0 + timedelta(days=1))

    @pytest.fixture(scope="class")
    def longitudes(self):
        return slice(-1, 6)

    @pytest.fixture(scope="class")
    def latitudes(self):
        return slice(37, 42)

    @pytest.fixture(scope="class")
    def data(self, times, longitudes, latitudes):
        data = Opendap("cmems_mod_glo_phy_anfc_merged-uv_PT1H-i")
        data.crop(None, times, longitudes, latitudes)
        return data

    @credentials
    def test_opendap(self, data):
        assert isinstance(data.ds, xr.Dataset)

    @credentials
    def test_crop(self, data, times, longitudes, latitudes):
        assert pd.Timestamp(data.ds.time.values.min()).to_pydatetime() <= times.start
        assert pd.Timestamp(data.ds.time.values.max()).to_pydatetime() >= times.stop
        assert data.ds.longitude.values.min() <= longitudes.start
        assert data.ds.longitude.values.max() >= longitudes.stop
        assert data.ds.latitude.values.min() <= latitudes.start
        assert data.ds.latitude.values.max() >= latitudes.stop

    @credentials
    def test_download(self, tmpdir, data):
        if not os.path.exists(tmpdir):
            os.makedirs(tmpdir.dirname)
        output_path = os.path.join(tmpdir, "test_netcdf.nc")
        paths = data.to_netcdf(output_path)
        ds = xr.open_mfdataset(paths)
        assert ds == data.ds

    @credentials
    def test_download_multiple(self, tmpdir, data):
        if not os.path.exists(tmpdir):
            os.makedirs(tmpdir.dirname)
        output_path = os.path.join(tmpdir, "test_netcdf.nc")
        paths = data._to_daily_netcdf(output_path)
        ds = xr.open_mfdataset(paths)
        assert ds == data.ds
