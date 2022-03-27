import json
import os


class FileNames:
    _cwd = os.getcwd()

    web_server_settings = os.path.join(_cwd, "config.json")
    secrets = os.path.join(_cwd, "settings.json")


class Settings:
    with open(FileNames.secrets, "r", encoding="utf-8") as _file:
        _data = json.load(_file)

    # giphy
    try:
        giphy_usage = _data["giphy"]["usage"]
        giphy_usage = True
    except KeyError:
        giphy_usage = False

    try:
        giphy_api_key = _data["giphy"]["api_key"]
    except KeyError:
        giphy_usage = False

    try:
        giphy_random = _data["giphy"]["random"]
        giphy_random_limit = _data["giphy"]["random"]
        giphy_trending = _data["giphy"]["trending"]
        giphy_trending_limit = _data["giphy"]["trending_limit"]
        giphy_api_url_base = _data["giphy"]["api_url_base"]
    except KeyError:
        giphy_random = False
        giphy_random_limit = 9
        giphy_trending = True
        giphy_api_url_base = "https://api.giphy.com/v1/gifs/"

    # picsum
    try:
        picsum_usage = _data["picsum"]["usage"]
    except KeyError:
        usage = False
    try:
        picsum_limit = _data["picsum"]["limit"]
    except KeyError:
        picsum_limit = 30

    try:
        picsum_api_url = _data["picsum"]["api_url"]
    except KeyError:
        picsum_api_url = "https://picsum.photos/200/300?random="


class Config:
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
