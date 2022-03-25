import json
import os


class FileNames:
    _cwd = os.getcwd()

    web_server_settings = os.path.join(_cwd, "config.json")


class Settings:
    _cwd = os.getcwd()

    with open(FileNames.web_server_settings, "r", encoding="utf-8") as _file:
        data = json.load(_file)

    try:
        host = data["host"]
        if not(len(str(host).split(".")) == 4):
            host = "0.0.0.0"
    except KeyError:
        host = "0.0.0.0"

    try:
        port = data["port"]
        try:
            port = int(port)
        except ValueError:
            port = 8080
    except KeyError:
        port = 8080

    try:
        debug = data["debug"]
        if isinstance(debug, str):
            if debug.lower() in ("true", "t", "yes", "y"):
                debug = True
            else:
                debug = False
        elif isinstance(debug, bool):
            pass
        else:
            debug = False
    except KeyError:
        debug = False
