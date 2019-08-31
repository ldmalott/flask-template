# {{cookiecutter.project_name}}

## Overview


## Installation

First, install `{{cookiecutter.project_slug}}` 
into the `pipenv` environment.  This will allow you
to use the CLI for the app.
```
pipenv run pip install -e .
```


## Usage

### From the command-line
You can then use `{{cookiecutter.project_slug}}` as
the command-line tool. It is a wrapper around `flask`
but creates the application without specifying environment
variables. Any command you can run after `flask` is
available to run as `{{cookiecutter.project_slug}}`.

*Examples*:
```
{{cookiecutter.project_slug}} run
{{cookiecutter.project_slug}} routes
{{cookiecutter.project_slug}} db migrate
```

### API
