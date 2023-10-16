========================================
Python Package and Notebook Cookiecutter
========================================

A project template for python projects and notebooks. This package is primarily intended for reserachers organize small projects
consisting of modules and notebooks.

To learn more about cookiecutter:

- Project Homepage: https://cookiecutter.readthedocs.io/en/latest/
- Github: https://github.com/audreyr/cookiecutter

Requirements for the Template
-----------------------------
- Python >= 3.5
- `Cookiecutter Python package <http://cookiecutter.readthedocs.org/en/latest/installation.html>`_ >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

::

  $ pip install cookiecutter

or ::

  $ conda install cookiecutter -c conda-forge


Starting a New Project
----------------------

If using for the first time or in need of a new clone: ::

  $ cookiecutter https://github.com/pcdshub/cookiecutter-pcds-python

or ::

  $ cookiecutter gh:pcdshub/cookiecutter-pcds-python

Otherwise: ::

  $ cookiecutter cookiecutter-pcds-python

Configuring a New Project
-------------------------

setuptools-scm automatically configures versioning for you, with no
setup steps required - when using pip.

Resulting Directory Structure
-----------------------------

The directory structure of your new project looks like this:

.. code-block:: text

  ├── .github/             <- GitHub templates and workflow settings
  │
  ├── {{ import_name }}    <- Source code for use in this project.
  │   │
  │   ├── __init__.py      <- Init file for the project
  │   │
  │   └── tests            <- Tests for the module
  │       │
  │       ├── __init__.py  <- Init file for the tests
  │       │
  │       └── conftest.py  <- Pytest conftest file
  │
  ├── docs                 <- A default Sphinx project; see sphinx-doc.org for details
  │
  ├── dev-requirements.txt <- Requirements to develop and test the package
  │
  ├── docs-requirements.txt <- Requirements to make the sphinx documentation
  │
  ├── .gitignore           <- Gitignore for the repo
  │
  ├── .logging.yml         <- Yaml configuration for Python logging
  │
  ├── LICENSE              <- License for the project
  │
  ├── MANIFEST.in          <- setup.py manifest of files
  │
  ├── README.rst           <- The top-level README for developers using this project
  │
  ├── requirements.txt     <- The requirements to install the project.
  │
  ├── run_tests.py         <- Script that runs the files in the tests directory


Installing Development Requirements
-----------------------------------
::

  $ pip install -Ur requirements.txt
  $ pip install -Ur dev-requirements.txt
  $ pip install -Ur docs-requirements.txt

Acknowledgements 
----------------
This repository is forked from from the work of SLAC National Accelerator Laboratory's controls team for the LCLS project. You can visit their original repository here: https://github.com/pcdshub/cookiecutter-pcds-python. 
