

include scripts/help.mk

dependencies: # Install dependencies needed to build and test the project @Pipeline
	poetry install

build: # Build the project artefact @Pipeline
	docker build -t "app:$$(git rev-parse HEAD)" .

deploy: # Deploy the project artefact to the target environment @Pipeline
	# TODO: Implement the artefact deployment step

clean:: # Clean-up project resources (main) @Operations
	# TODO: Implement project resources clean-up step

config: config_asdf config_precommit config_poetry # Configure development environment (main) @Configuration


test: test-unit test-lint # Run all tests @Testing

test-unit: # Run unit tests @Testing
	DEBUG=1 poetry run pytest

test-lint: # Lint files @Testing
	# TODO

test-ui: # Run UI tests @Testing
	# TODO

run: manage_breast_screening/config/.env # Run the development server @Development
	poetry run ./manage.py runserver

config_asdf:
	if ! command -v asdf >/dev/null 2>&1; then \
		echo "asdf is not installed; install it from https://github.com/asdf-vm/asdf" \
		exit 1; \
	fi
	asdf plugin add python

config_precommit:
	if ! command -v pre-commit >/dev/null 2>&1; then \
		echo "pre-commit is not installed; install it from https://pre-commit.com/" \
		exit 1; \
	fi
	pre-commit install

config_poetry:
	if ! command -v poetry >/dev/null 2>&1; then \
		pip install poetry; \
	else \
		echo "poetry already installed"; \
	fi


help: # Print help @Others
	printf "\nUsage: \033[3m\033[93m[arg1=val1] [arg2=val2] \033[0m\033[0m\033[32mmake\033[0m\033[34m <command>\033[0m\n\n"
	perl -e '$(HELP_SCRIPT)' $(MAKEFILE_LIST)


manage_breast_screening/config/.env:
	cp manage_breast_screening/config/.env.tpl manage_breast_screening/config/.env


.DEFAULT_GOAL := help
.ONESHELL:
.PHONY: dependencies build deploy clean config test test-unit test-lint test-ui run config_asdf config_poetry config_precommit help
.SILENT: help config config_precommit config_asdf config_poetry
MAKEFLAGS := --no-print-directory
SHELL := /bin/bash