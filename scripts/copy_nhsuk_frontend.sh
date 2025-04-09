#!/bin/bash

cp -r node_modules/nhsuk-frontend/packages/{components,macros,assets} manage_breast_screening/templates/

cp -r node_modules/nhsuk-frontend/dist/nhsuk-* manage_breast_screening/static/