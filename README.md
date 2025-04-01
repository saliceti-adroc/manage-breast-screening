# Manage breast screening Django spike

[![CI/CD Pull Request](https://github.com/nhs-england-tools/repository-template/actions/workflows/cicd-1-pull-request.yaml/badge.svg)](https://github.com/nhs-england-tools/repository-template/actions/workflows/cicd-1-pull-request.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=repository-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=repository-template)

This repo is a spike to explore using Django as the framework for our new service.

The new service is a system for managing breast screening clinics, including:

- Viewing and managing daily clinic lists
- Tracking participants through their screening journey
- Managing participant information and status

## Setup

To install the toolchain dependencies, run

```shell
make config
```

This command assumes you have a few things already installed:

- [Docker](https://www.docker.com/) container runtime or a compatible tool, e.g. [Podman](https://podman.io/)
- [asdf](https://asdf-vm.com/) version manager
- [GNU make](https://www.gnu.org/software/make/) 3.82 or later

## Usage

If dependencies have been installed correctly, you shoul dbe able to run

```sh
poetry install
poetry run ./manage.py migrate
poetry run ./manage.py runserver
```

Alternatively, you can use the `make` shortcuts:

```sh
make dependencies
make run
```

### Testing

```sh
make test
```

## Design

### Structure

The `manage_breast_screening` directory contains all the Django project code.

`config` is a subpackage containing the configuration. The other subpackages - such as `clinics` - are [Django apps](https://docs.djangoproject.com/en/5.1/ref/applications/). These each represent a bounded context within our overall domain of screening events. Django apps can be built with customisability and extendability in mind, and published as python packages, but we aren't doing that yet.

To generate a new app, run:

```sh
poetry run ./manage.py startapp <app_name> manage_breast_screening/`
```

## Contributing

- Make sure you have `pre-commit` running so that pre-commit hooks run automatically when you commit - this should have been set up automatically when you ran `make config`.
- Consider switching on format-on-save in your editor (e.g. [Black](https://github.com/psf/black) for python)
- (Internal contributions only) contact the `#screening-manage` team on slack with any questions

## Licence
Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample code in the documentation. See [LICENCE.md](./LICENCE.md).

Any HTML or Markdown documentation is [© Crown Copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
