import json
import os
import requests


# The file names and paths of the needed json config files and others
class FileNames:
    _cwd = os.getcwd()

    def _check_database_exist():
        database_folder = os.path.join(os.getcwd(), "database")
        if not(os.path.isdir(database_folder)):
            os.makedirs(database_folder)
        else:
            files = [
                {
                    "url": "https://raw.githubusercontent.com/hirusha-adi/GifGang/main/web/database/config.json",
                    "filename": "config.json"
                },
                {
                    "url": "https://raw.githubusercontent.com/hirusha-adi/GifGang/main/web/database/important.json",
                    "filename": "important.json"
                },
                {
                    "url": "https://raw.githubusercontent.com/hirusha-adi/GifGang/main/web/database/website.json",
                    "filename": "website.json"
                }
            ]

            for file in files:
                if isinstance(file, dict):
                    r = requests.get(file["url"])
                    with open(os.path.join(database_folder, file["filename"]), "wb") as makefile:
                        makefile.write(r.content)

    _check_database_exist()

    web_server_settings = os.path.join(_cwd, "database", "config.json")
    important_info_file = os.path.join(_cwd, "database", "important.json")
    website_info_file = os.path.join(_cwd, "database", "website.json")

    print(f"[+] Detected `config.json` at {web_server_settings}")
    print(f"[+] Detected `settings.json` at {important_info_file}")
    print(f"[+] Detected `website.json` at {website_info_file}")


# Store website data
class WebsiteData:
    with open(FileNames.website_info_file, "r", encoding="utf-8") as _file:
        _data = json.load(_file)
        print("[+] Loaded `website.json`")

    age_verify = _data["age_verify"]
    index = _data["index"]
    pins = _data["pins"]
    search = _data["search"]
    adult_index = _data["adult_index"]
    adult_pins = _data["adult_pins_and_categories"]
    adult_stars = _data["adult_stars"]
    adult_search = _data["adult_search"]
    adult_hentai = _data["adult_hentai"]


# Store the main website settings like API keys, etc...
class Important:
    with open(FileNames.important_info_file, "r", encoding="utf-8") as _file:
        _data = json.load(_file)

        print("[+] Loaded `secrets.json`")

    # SFW
    _giphy = _data["giphy"]
    giphy_usage = _giphy["usage"]
    giphy_api_url_base = _giphy["api_url_base"]
    giphy_api_key = _giphy["api_key"]

    _picsum = _data["picsum"]
    picsum_usage = _picsum["usage"]
    picsum_api_url_base = _picsum["api_url_base"]

    _tenor = _data["tenor"]
    tenor_usage = _tenor["usage"]
    tenor_api_key = _tenor["api_key"]

    _unsplash = _data["unsplash"]
    unsplash_usage = _unsplash["usage"]
    unsplash_api_key = _unsplash["api_key"]

    _thecatapi = _data["theCatAPI"]
    thecatapi_usage = _thecatapi["usage"]

    _dogceo = _data["dogCEO"]
    dogceo_usage = _dogceo["usage"]

    _nekoslife = _data["nekoslife"]
    nekoslife_usage = _nekoslife["usage"]

    _imgur = _data["imgur"]
    imgur_usage = _imgur["usage"]
    imgur_auth_key = _imgur["auth_key"]
    imgur_client_id = _imgur["client_id"]
    imgur_clinet_secret = _imgur["clinet_secret"]

    # NSFW
    _eporner = _data["eporner"]
    eporner_usage = _eporner["usage"]

    _redtube = _data["redtube"]
    redtube_usage = _redtube["usage"]

    _localserverml = _data["localserverml"]
    localserverml_usage = _localserverml["usage"]


# Settings needed for hosting the website
class Config:
    with open(FileNames.web_server_settings, "r", encoding="utf-8") as _file:
        data = json.load(_file)
        print("[+] Loaded `config.json`")

    try:
        host: str = data["host"]
        if not(len(str(host).split(".")) == 4):
            host: str = "0.0.0.0"
    except KeyError:
        host: str = "0.0.0.0"

    try:
        port = data["port"]
        try:
            port: int = int(port)
        except ValueError:
            port: int = 8080
    except KeyError:
        port: int = 8080

    try:
        debug = data["debug"]
        if isinstance(debug, str):
            if debug.lower() in ("true", "t", "yes", "y"):
                debug: bool = True
            else:
                debug: bool = False
        elif isinstance(debug, bool):
            pass
        else:
            debug: bool = False
    except KeyError:
        debug: bool = False

    try:
        DEV = data["dev_mode"]
        if isinstance(DEV, str):
            if DEV.lower() in ("true", "t", "yes", "y"):
                DEV: bool = True
            else:
                DEV: bool = False
        elif isinstance(DEV, bool):
            pass
        else:
            DEV: bool = False
    except KeyError:
        DEV: bool = False


def log(message: str, ipaddr: str = False, mode: str = "DEBUG"):
    if Config.DEV:
        if not(ipaddr):
            print(f'[{mode}]: {message}')
        if (mode and ipaddr):
            print(f'[{mode}][{ipaddr}]: {message}')
