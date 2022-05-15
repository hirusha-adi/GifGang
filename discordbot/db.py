import json
import os

from src.utils import Filenames


class Config:
    with open(Filenames.config_json, "r", encoding="utf-8") as _file:
        data = json.load(_file)

    prefix = data["prefix"]
    admins = data["admins"]
    channels = data["channels"]
    channels_nsfw = channels["nsfw"]
