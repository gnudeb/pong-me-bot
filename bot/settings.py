"""
This file contains project-wide settings.
Settings variables that are created in this file
must be CAPITALIZED_WITH_UNDERSCORES
"""
import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")

with open(SETTINGS_PATH, 'r') as secrets_file:
    settings = json.load(secrets_file)
    TG_TOKEN = settings["TG_TOKEN"]
