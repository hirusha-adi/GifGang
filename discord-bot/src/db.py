import os
import json
from src.utils import Filenames


class Config:
    with open(Filenames.config_json, "r", encoding="utf-8") as _file:
        data = json.load(_file)
