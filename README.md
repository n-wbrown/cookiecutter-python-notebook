# Python Package and Notebook Cookiecutter

A project template for python projects and notebooks. This template is intended for researchers to organize small projects consisting of modules and notebooks.

To learn more about cookiecutter:

- Cookiecutter Homepage: https://cookiecutter.readthedocs.io/en/latest/
- Github: https://github.com/audreyr/cookiecutter

## Project Status

| Branch      | Status      |
| ----------- | ----------- |
| Main        | [![main](https://github.com/n-wbrown/cookiecutter-python-notebook/actions/workflows/cookiecutter-test.yml/badge.svg?branch=main)](https://github.com/n-wbrown/cookiecutter-python-notebook/actions?query=branch%3Amain) |
| Dev         | [![dev](https://github.com/n-wbrown/cookiecutter-python-notebook/actions/workflows/cookiecutter-test.yml/badge.svg?branch=dev)](https://github.com/n-wbrown/cookiecutter-python-notebook/actions?query=branch%3Adev) |

## Requirements for the Template
- Python >= 3.8
- `Cookiecutter Python package <http://cookiecutter.readthedocs.org/en/latest/installation.html>`_ >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

```
  $ pip install cookiecutter
```

or

```
  $ conda install cookiecutter -c conda-forge
```

## Starting a New Project

If using for the first time or in need of a new clone:

```
  $ cookiecutter https://github.com/n-wbrown/cookiecutter-python-notebook
```

or

```
  $ cookiecutter gh:n-wbrown/cookiecutter-python-notebook
```

Otherwise:

```
  $ cookiecutter cookiecutter-python-notebook
```

For using a specific git tag of the cookiecutter, append the `--checkout [version]` option and supply the intended git tag name:

```
  $ cookiecutter cookiecutter-python-notebook --checkout v0.2
```

## Configuring a New Project

setuptools-scm automatically configures versioning for you, with no
setup steps required - when using pip.

## Resulting Directory Structure

The directory structure of your new project looks like this:

```
  │
  ├── .gitignore            <- Gitignore for the repo (https://git-scm.com/docs/gitignore)
  │
  ├── {{ import_name }}     <- Source code for use in this project
  │   │
  │   ├── __init__.py       <- Init file for the project
  │   │
  │   └── tests             <- Tests for the module
  │       │
  │       ├── __init__.py   <- Init file for the tests
  │       │
  │       └── conftest.py   <- Pytest conftest file
  │
  ├── pyproject.toml        <- Contains configuration and packaging information about your project
  │
  ├── .logging.yml          <- Yaml configuration for Python logging
  │
  ├── LICENSE               <- License for the project
  │
  ├── MANIFEST.in           <- setup.py manifest of files
  │
  ├── README.rst            <- The top-level README for developers using this project
  │
  ├── requirements.txt      <- The requirements to install the project.
  │
  ├── .github/              <- (Optional) GitHub templates and workflow settings
  │
  ├── docs                  <- (Optional) A default Sphinx project; see sphinx-doc.org for details
  │
  ├── data                  <- (Optional) An empty directory for data and links
  │
  ├── output                <- (Optional) An empty directory for results
  │
  ├── dev-requirements.txt  <- (Optional) Requirements to develop the package and execute the test suite
  │
  ├── docs-requirements.txt <- (Optional) Requirements to generate the sphinx documentation
```


## Installing Development Requirements

The following commands can be used to install the packages necessary for running, developing, and building the documentation for your new package respectively. Run these commands in the main directory of your newly created package.

```
  $ pip install -Ur requirements.txt
  $ pip install -Ur dev-requirements.txt
  $ pip install -Ur docs-requirements.txt
```

## Acknowledgements 
This repository is forked from from the work of SLAC National Accelerator Laboratory's controls team for the LCLS project. You can visit their original repository here: https://github.com/pcdshub/cookiecutter-pcds-python. 
