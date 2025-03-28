#!/bin/sh
echo "Installing dependencies from mise toml"
mise trust --all
mise install --verbose
echo "Setting up uv"
mise exec -- uv venv --native-tls --verbose
mise exec -- uv sync
mise exec -- uv run pre-commit install
