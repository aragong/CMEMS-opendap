# MetOceanProviders
Access to main open-access MetOcean products (Forecast, Reanalysis and other type of atmospheric and oceaninc databases) 


# TESEO.Apiprocess
Python-Flask Api to trigger TESEO simulations. This development preprocess, execute and postprocess [TESEO](https://github.com/IHCantabria/TESEO) simulations to provide standard outputs in .nc .json .geojson and .csv formats. Forcing input information accepted is in standard netcdf format. Oil-substance information is also included in this repository, see this [section](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/teseo_apiprocess/substances/README.md).

![GitHub top language](https://img.shields.io/github/languages/top/IHCantabria/TESEO.Apiprocess?style=plastic)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/IHCantabria/TESEO.Apiprocess?label=latest%20tag&style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/IHCantabria/TESEO.Apiprocess?style=plastic)
![GitHub](https://img.shields.io/github/license/IHCantabria/TESEO.Apiprocess?style=plastic)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/IHCantabria/TESEO.Apiprocess)
![CI](https://github.com/IHCantabria/TESEO.Apiprocess/actions/workflows/main.yml/badge.svg)
![Coverage](coverage.svg)

---
## :zap: Get Started

- Launch the Api and use it (check Swagger)

Bash:
``` bash
$ export FLASK_APP=teseo_apiprocess.api
$ flask run
* Running on http://127.0.0.1:5000/
```

CMD:
``` cmd
> set FLASK_APP=teseo_apiprocess.api
> flask run
* Running on http://127.0.0.1:5000/
```

Powershell:
``` powershell
> $env: FLASK_APP="teseo_apiprocess.api"
> $ flask run
* Running on http://127.0.0.1:5000/
```

- Run the python module and main methods orovided in [main.py](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/teseo_apiprocess/main.py):

    - run_simulation(substance_type, input_json)
    - get_substances(substance_type)



## :package: Package structure
Reminder--> *command: `tree --dirsfirst -ACQ -I __pycache__`*

```
TESEO.Apiprocess
.
├── "bin"
│   └── "teseo"
├── "data"
│   ├── "domains"
│   └── "imgs"
├── "teseo_apiprocess"
│   ├── "substances"
│   │   ├── "templates"
│   │   ├── "README.md"
│   │   ├── "__init__.py"
│   │   ├── "hns.json"
│   │   ├── "oil.json"
│   │   └── "utils.py"
│   ├── "utils"
│   │   ├── "__init__.py"
│   │   ├── "api_doc.py"
│   │   ├── "case_type_converter.py"
│   │   ├── "get_uuid.py"
│   │   ├── "logger.py"
│   │   ├── "serialize_datatime.py"
│   │   └── "teseo.py"
│   ├── "__init__.py"
│   ├── "api.py"
│   ├── "config.py"
│   ├── "downloader.py"
│   ├── "inputs.py"
│   ├── "job.py"
│   ├── "main.py"
│   └── "outputs.py"
├── "tests"
│   ├── "integration"
│   │   ├── "__init__.py"
│   │   ├── "test_api.py"
│   │   ├── "test_downloaders.py"
│   │   └── "test_main.py"
│   ├── "unit"
│   │   ├── "__init__.py"
│   │   ├── "test_inputs.py"
│   │   ├── "test_job.py"
│   │   ├── "test_outputs.py"
│   │   ├── "test_substances.py"
│   │   └── "test_utils.py"
│   ├── "utils"
│   │   ├── "templates"
│   │   │   ├── "drifter_2d_single.json"
│   │   │   ├── "drifter_2d_single_back.json"
│   │   │   ├── "drifter_2d_single_multiple.json"
│   │   │   ├── "hns_2d_continuous.json"
│   │   │   ├── "hns_2d_single.json"
│   │   │   ├── "hns_2d_single_back.json"
│   │   │   ├── "hns_2d_single_multiple.json"
│   │   │   ├── "oil_2d_continuous.json"
│   │   │   ├── "oil_2d_single.json"
│   │   │   ├── "oil_2d_single_back.json"
│   │   │   ├── "oil_2d_single_multiple.json"
│   │   │   ├── "oil_q3d_continuous.json"
│   │   │   ├── "oil_q3d_single.json"
│   │   │   └── "test_be_ready_spezia.json"
│   │   └── "data.zip"
│   └── "__init__.py"
├── "CHANGELOG.md"
├── "DEPLOY_REQUIREMENTS.md"
├── "DOCUMENTATION.md"
├── "LICENSE"
├── "README.md"
├── "api.wsgi"
├── "coverage.svg"
├── "environment.yml"
├── "pyproject.toml"
├── "requirements.in"
└── "requirements.txt"
```

## :house: Local installation
* Using conda + pip:
```bash
# Create conda env and install python libreries
conda env create --file environment.yml --name python-env

# Activate virtual env
conda activate python-env
```

* Using venv + pip:
```bash
# # Create virtual env
python3.6 -m venv env --clear

# # Activate virtual env
source env/bin/activate

# # Install dependencies
python -m pip install -r requirements.txt
```
---
## :recycle: Continuous integration (CI)

* Pre-commit with **black formatter** hook on `commit`. ([.pre-commit-config.yaml](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.pre-commit-config.yaml))
* Github workflow with conda based **deployment** and **testing** on `tag`. ([Github action](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.github/workflows/main.yml))
* Test and update coverage badge **manually** through vscode [task](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.vscode/tasks.json): `run test and coverage`


---
## :heavy_check_mark: Testing
* To run tests manually:
```bash
# Unzip data for testing stored in "data.zip" in "tests/" folder
7z x tests/data.zip -otests/ 

# Run pytests from console
pytest
```
* **Update coverage badge manually** through vscode task `run test and coverage` or running:
```bash
pytest --cov=./
coverage-badge -o coverage.svg -f
```

---

## :rocket: Package deployment
Check [DEPLOY_REQUIREMENTS.md](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/DEPLOY_REQUIREMENTS.md) for a full detailed explanation.

---
## :incoming_envelope: Contact us
:snake: For code-development issues contact :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria)

## :copyright: Credits
Developed by :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria).
