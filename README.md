# Met-ocean providers
![GitHub top language](https://img.shields.io/github/languages/top/aragong/metoceanproviders?style=plastic)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/aragong/metoceanproviders?label=latest%20tag&style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/aragong/metoceanproviders?style=plastic)
![GitHub](https://img.shields.io/github/license/aragong/metoceanproviders?style=plastic)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/aragong/metoceanproviders)
![Coverage](coverage.svg)

Python package to access main open-access met-ocean products (Forecast, Reanalysis and other type of atmospheric and oceaninc databases) from general providers (CMEMS, NOAA...)

---
## :house: Installation
```bash
pip install git+ssh://git@github.com/aragong/metoceanproviders.git@v0.1.0

# Declare CMEMS_USERNAME and CMEMS_PASSWORD variables
dotenv set CMEMS_USERNAME your_cmems_username
dotenv set CMEMS_PASSWORD your_cmems_password
```

---
## :zap: Get Started

```python
import metoceanproviders.cmems as cmems

# EXAMPLE for accessing CMEMS opendap products
data = cmems.Opendap(dataset_id, username, password)

data.ds # To visualize connected xarray dataset.
data.crop(varaibles, times, longitudes, latitudes) # To crop dataset.
data.to_netcdf(output_path) # To download to NetCDF-file.
```

---
## :recycle: Continuous integration (CI)

* Pre-commit with **black formatter** hook on `commit`. ([.pre-commit-config.yaml](https://github.com/aragong/metoceanproviders/blob/main/.pre-commit-config.yaml))
* Github workflow with conda based **deployment** and **testing** on `tag`. ([Github action](https://github.com/aragong/metoceanproviders/blob/main/.github/workflows/main.yml))
* Test and update coverage badge **manually** through vscode [task](https://github.com/aragong/metoceanproviders/blob/main/.vscode/tasks.json): `run test and coverage`
---
## :incoming_envelope: Contact us
:snake: For code-development issues contact :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria)

## :copyright: Credits
Developed by :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria).
