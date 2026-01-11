#!/bin/bash
# Run as an Xwayland app, that makes the window borders look better, and allows forceing always on top by default.
QT_QPA_PLATFORM=xcb poetry run python main.py https://cluetrainer.app/appconfig.json
