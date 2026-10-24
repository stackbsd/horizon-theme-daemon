"""Daemon theme for the OpenStack dashboard."""

import os
import pathlib

THEME_PATH = str(pathlib.Path(__file__).resolve().parent / "theme")
THEMES = [
    ("daemon", "Daemon", THEME_PATH),
    ("daemon-dark", "Daemon Dark", os.path.join(THEME_PATH, os.curdir)),
]
