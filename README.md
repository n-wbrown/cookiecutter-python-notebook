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

## Starting a New Project with this Template: A Step-by-Step Guide

### 1. Obtain and Execute the Template

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

### Selecting Configuration Options

After running the `cookiecutter ...` command, you will be prompted with a series of questions. Your answers will structure the contents of the repository. 

#### Important Options
These options should be considered carefully when setting up the project. They may affect how the package and repository are referenced and may be difficult to change later.

- `project_name`: This sets the human-readable name for your project.
- `repo_name`: The name of the github repository will be used if `auto_git_setup` is configured (e.g. `cookiecutter-python-notebook`)
- `author_name`: This name will be visible in the documentation.
- `email`: Contact email for the primary author.
- `folder_name`: Set the name of development folder.
- `github_repo_group`: The name for the parent organization of the github repository. This typically is either the author's github name (e.g `n-wbrown`) or the organization that owns the github repository.
- `import_name`: The name to use when importing this package in python. Defaults to the folder name.

#### Additional Options
These options are less critical and can be easily configured at a later time. For those in a hurry or those who may be unsure what all these options do, the defaults will be sufficient for most use cases.

- `description`: Provide a short human-readable description of the project that will appear at the top of the readme.
- `python_version`: Select the python version to specify for this project. Most users of the package will treat this as a minimum requirement.
- `auto_git_setup`: Select "yes" to automatically connect the local git folder with a github repository and add the initial files for committing. At this time, git services other than github have not been tested. 
- `git_remote_name`: Set the name of git remote. (See `git remote` [documentation](https://git-scm.com/docs/git-remote) for details)
- `readme_format`: Choose the format of the readme file to use.
- `simple`: Simple omits most CI tools and additional organization folders.
- `strip_ipynb_outputs`: Selecting yes includes a hook to remove output from juypter notebooks before committing. Selecting "no" is strongly recommended. See this [section](Committing_Jupyter_Notebook_Output) for more details.

Once the package has been configured via the questionnaire. Your new package will be created in a new directory matching the `folder_name` option.

### Setting up the package for development and use

First create a new virtual environment or activate a preexisting environment on your system. Using [venv](https://docs.python.org/3/library/venv.html) or [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) is recommended.

To install the package for development in your environment:

```
$ pip install -e <path_to_your_package>
```

### Configuring a New Project

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

## Committing Jupyter Notebook Output

This repository had the option to preserve the results of jupyter notebooks. This is generally not recommended to keep repository sizes manageable. To create an exception to this rule, if the "yes" option has been selected for the `strip_ipynb_outputs` setting, use `git -c filter.strip-notebook-output.clean= add <path to your notebook>`. See this [thread](https://gist.github.com/33eyes/431e3d432f73371509d176d0dfb95b6e) for more details. To prevent this behavior entirely, select "no" for the `strip_ipynb_outputs` setting. For those wishing to undo the "yes" setting and preserve jupyter output by default, remove this line `*.ipynb filter=strip-notebook-output` from the 


## Acknowledgements 
This repository is forked from the work of SLAC National Accelerator Laboratory's controls team for the LCLS project. You can visit their original repository here: https://github.com/pcdshub/cookiecutter-pcds-python. 
