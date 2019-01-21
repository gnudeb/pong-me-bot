import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")

with open(SETTINGS_PATH, 'r') as f:
    settings = json.load(f)
    TG_TOKEN = settings["TG_TOKEN"]


DEFAULT_REPLY_INTERVAL = 5
