import os


class Filenames:
    _cwd = os.getcwd()
    config_json = os.path.join(_cwd, "database", "config.json")
