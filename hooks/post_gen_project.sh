#!/bin/bash
git init
{% if cookiecutter.auto_git_setup == "yes" %}
git add -A
git remote add {{ cookiecutter.git_remote_name }} git@github.com:{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}.git
git commit -am "Initial commit from cookiecutter-python-notebook"
{% endif %}
