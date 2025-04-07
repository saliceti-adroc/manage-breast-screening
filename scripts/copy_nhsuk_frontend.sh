#!/bin/bash

cp -r node_modules/nhsuk-frontend/packages/{components,macros} manage_breast_screening/templates/
cp -r node_modules/nhsuk-frontend/packages/assets manage_breast_screening/static/
cp -r node_modules/nhsuk-frontend/dist/nhsuk-* manage_breast_screening/static/
