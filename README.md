# Wagtail streamfield-validator

A Wagtail StreamField JSON validation provider.

[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI version](https://badge.fury.io/py/wagtail-streamfield-validator.svg)](https://badge.fury.io/py/wagtail-streamfield-validator)
[![streamfield-validator CI](https://github.com/wagtail/wagtail-streamfield-validator/actions/workflows/test.yml/badge.svg)](https://github.com/wagtail/wagtail-streamfield-validator/actions/workflows/test.yml)

## Introduction

This is a very early project, and it is not yet ready for production use. It is a work in progress.

This project seeks to address/implement https://github.com/wagtail/wagtail/issues/6495.

The goal of this project is to provide a way to validate the JSON structure of a Wagtail StreamField.
This is useful when you want to generate or modify StreamField content programmatically, and you want
to ensure that the content is valid before saving it to the database.

The immediate next steps for the project are:

1. Ability to generate a JSON schema from a StreamField definition.
2. Ability to validate a JSON object against the generated schema.
3. Ability to install the JSON schema as a validator on the StreamField's model JSONField.
4. Ability to install the JSON schema as a validator on a rest_framework endpoint.

The project should be built in a way that it can be used to produce other validation formats than
JSON schema. For example, one might like to generate a Pydantic model to use for programmatic
validation of the StreamField content.

This project might potentially use the following packages:

- [jsonschema](https://pypi.org/project/jsonschema/)
- [pydantic](https://pypi.org/project/pydantic/)
- [datamodel-code-generator](https://pypi.org/project/datamodel-code-generator/)
- https://plugins.jetbrains.com/plugin/12861-pydantic

Also note these

- https://github.com/wagtail/wagtail-streamfield-migration-toolkit/blob/main/wagtail_streamfield_migration_toolkit/autodetect/streamchangedetector.py

## Links

- [Documentation](https://github.com/wagtail/wagtail-streamfield-validator/blob/main/README.md)
- [Changelog](https://github.com/wagtail/wagtail-streamfield-validator/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/wagtail/wagtail-streamfield-validator/blob/main/CONTRIBUTING.md)
- [Discussions](https://github.com/wagtail/wagtail-streamfield-validator/discussions)
- [Security](https://github.com/wagtail/wagtail-streamfield-validator/security)

## Supported versions

- Python 3.10, 3.11, 3.12
- Django 4.2, 5.0, 5.1
- Wagtail 4.1, 5.2, 6.0, 6.1

## Installation

- `python -m pip install wagtail-streamfield-validator`
- ...

## Contributing

### Install

To make changes to this project, first clone this repository:

```sh
git clone https://github.com/wagtail/wagtail-streamfield-validator.git
cd wagtail-streamfield-validator
```

With your preferred virtualenv activated, install testing dependencies:

#### Using pip

```sh
python -m pip install --upgrade pip>=21.3
python -m pip install -e '.[testing]' -U
```

#### Using flit

```sh
python -m pip install flit
flit install
```

### pre-commit

Note that this project uses [pre-commit](https://github.com/pre-commit/pre-commit).
It is included in the project testing requirements. To set up locally:

```shell
# go to the project directory
$ cd wagtail-streamfield-validator
# initialize pre-commit
$ pre-commit install

# Optional, run all checks once for this, then the checks will run only on the changed files
$ git ls-files --others --cached --exclude-standard | xargs pre-commit run --files
```

### How to run tests

Now you can run tests as shown below:

```sh
tox
```

or, you can run them for a specific environment `tox -e python3.11-django4.2-wagtail5.1` or specific test
`tox -e python3.11-django4.2-wagtail5.1-sqlite wagtail-streamfield-validator.tests.test_file.TestClass.test_method`

To run the test app interactively, use `tox -e interactive`, visit `http://127.0.0.1:8020/admin/` and log in with `admin`/`changeme`.
