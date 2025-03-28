

include scripts/help.mk

dependencies: # Install dependencies needed to build and test the project @Pipeline
	poetry install

build: # Build the project artefact @Pipeline
	# TODO: Implement the artefact build step

deploy: # Deploy the project artefact to the target environment @Pipeline
	# TODO: Implement the artefact deployment step

clean:: # Clean-up project resources (main) @Operations
	# TODO: Implement project resources clean-up step

config: config_asdf config_precommit # Configure development environment (main) @Configuration

test: # Run all tests
	poetry run pytest


test-lint: # Lint files
	echo "Not configured"

run:
	poetry run ./manage.py runserver

config_asdf:
	if ! command -v asdf >/dev/null 2>&1; then \
		echo "asdf is not installed; install it from https://github.com/asdf-vm/asdf" \
		exit 1; \
	fi

config_precommit:
	if ! command -v pre-commit >/dev/null 2>&1; then \
		echo "pre-commit is not installed; install it from https://pre-commit.com/" \
		exit 1; \
	fi
	pre-commit install

help: # Print help @Others
	printf "\nUsage: \033[3m\033[93m[arg1=val1] [arg2=val2] \033[0m\033[0m\033[32mmake\033[0m\033[34m <command>\033[0m\n\n"
	perl -e '$(HELP_SCRIPT)' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
.ONESHELL:
.PHONY: *
.SILENT: help
MAKEFLAGS := --no-print-directory
SHELL := /bin/bash