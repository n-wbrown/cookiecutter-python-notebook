"""
Delete non-essential directories for simple-case setup. 

Script taken from https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html
"""

import os
import shutil


REMOVE_PATHS = [
    '{% if cookiecutter.simple == "yes" %}.github{% endif %}',
    '{% if cookiecutter.simple == "yes" %}conda-recipe{% endif %}',
    '{% if cookiecutter.simple == "yes" %}docs{% endif %}',
]


def remove_paths():
    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)


if __name__ == "__main__":
    remove_paths()