#!/bin/bash
# Commands needed to fix after updating Ubuntu versions.
rm -rf poetry.lock
rm -rf .venv
poetry install