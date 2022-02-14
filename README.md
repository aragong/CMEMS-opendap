# MetOceanProviders
Python package to access main open-access MetOcean products (Forecast, Reanalysis and other type of atmospheric and oceaninc databases) from general providers (CMEMS, NOAA, )


![GitHub top language](https://img.shields.io/github/languages/top/aragong/MetOceanProviders?style=plastic)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/aragong/MetOceanProviders?label=latest%20tag&style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/aragong/MetOceanProviders?style=plastic)
![GitHub](https://img.shields.io/github/license/aragong/MetOceanProviders?style=plastic)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/aragong/MetOceanProviders)
![Coverage](coverage.svg)

## :house: Installation
```
pip install git+ssh://git@github.com/aragong/qualitas.downloader.git@v0.1.0
```

---
## :zap: Get Started

```python
import metocean_providers as mop

# EXAMPLE for accessing CMEMS opendap products
data = mop.cmems.Opendap(dataset_id, username, password)

data.ds # To visualize connected xarray dataset.
data.crop(varaibles, times, longitudes, latitudes, depths) # To crop dataset.
datato_netcdf(output_path) # To download to NetCDF-file.
```

---
## :recycle: Continuous integration (CI)

* Pre-commit with **black formatter** hook on `commit`. ([.pre-commit-config.yaml](https://github.com/aragong/MetOceanProviders/blob/main/.pre-commit-config.yaml))
* Github workflow with conda based **deployment** and **testing** on `tag`. ([Github action](https://github.com/aragong/MetOceanProviders/blob/main/.github/workflows/main.yml))
* Test and update coverage badge **manually** through vscode [task](https://github.com/aragong/MetOceanProviders/blob/main/.vscode/tasks.json): `run test and coverage`
---
## :incoming_envelope: Contact us
:snake: For code-development issues contact :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria)

## :copyright: Credits
Developed by :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria).
