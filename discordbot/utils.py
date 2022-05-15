import os


class Filenames:
    _cwd = os.getcwd()
    config_json = os.path.join(_cwd, "database", "discordbot.json")
    token_txt = os.path.join(_cwd, "token.txt")
