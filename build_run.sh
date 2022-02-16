#!/bin/bash
pipenv run poetry run make dev && pipenv run poetry run python main.py --remote-debugging-port=9222 https://runeapps.org/apps/clue/appconfig.json
