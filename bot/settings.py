"""
This file contains project-wide settings.
Settings variables that are created in this file
must be CAPITALIZED_WITH_UNDERSCORES
"""
import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRETS_PATH = os.path.join(BASE_DIR, "secrets.json")

with open(SECRETS_PATH, 'r') as secrets_file:
    secrets = json.load(secrets_file)
    TG_TOKEN = secrets["TG_TOKEN"]
