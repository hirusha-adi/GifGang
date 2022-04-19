import json
import os
import requests
import random


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

    # _check_database_exist()

    web_server_settings = os.path.join(_cwd, "database", "config.json")
    important_info_file = os.path.join(_cwd, "database", "important.json")
    website_info_file = os.path.join(_cwd, "database", "website.json")
    count_file = os.path.join(_cwd, "count.txt")

    print(f"[+] Detected `config.json` at {web_server_settings}")
    print(f"[+] Detected `settings.json` at {important_info_file}")
    print(f"[+] Detected `website.json` at {website_info_file}")
    print(f'Visit count file will be at {count_file}')


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

    _thecatapi = _data["theCatAPI"]
    thecatapi_usage = _thecatapi["usage"]

    _dogceo = _data["dogCEO"]
    dogceo_usage = _dogceo["usage"]

    _nekoslife = _data["nekoslife"]
    nekoslife_usage = _nekoslife["usage"]

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


class Process:

    def index_Giphy(request):
        giphy_url_list = []
        giphy_usage = False
        if Important.giphy_usage:
            if WebsiteData.index["api_usage"]["giphy"]["usage"]:
                giphy_usage = True

                # Random
                if WebsiteData.index["api_usage"]["giphy"]["random"]:
                    for _ in range(int(WebsiteData.index["api_usage"]["giphy"]["random_limit"])):
                        r = requests.get(
                            f'{WebsiteData.index["api_usage"]["giphy"]["random_api_url"]}?api_key={Important.giphy_api_key}')
                        if 300 > r.status_code >= 200:
                            try:
                                data = r.json()
                                giphy_url_list.append(
                                    {
                                        "url": data["data"]["images"]["original"]["url"],
                                        "title": data["data"]["title"]
                                    }
                                )
                            except Exception as e:
                                print(e)

                    log(
                        f'GIPHY: Random One by One: True - {int(WebsiteData.index["api_usage"]["giphy"]["random_limit"])}',
                        ipaddr=request.remote_addr)

                # Trending
                if WebsiteData.index["api_usage"]["giphy"]["trending"]:
                    offset = random.randint(
                        1, 4990 - int(WebsiteData.index["api_usage"]["giphy"]["trending_limit"]))
                    r = requests.get(
                        f'{WebsiteData.index["api_usage"]["giphy"]["trending_api_url"]}?api_key={Important.giphy_api_key}&limit={WebsiteData.index["api_usage"]["giphy"]["trending_limit"]}&offset={offset}')
                    if 300 > r.status_code >= 200:
                        try:
                            data = r.json()
                            for item in data["data"]:
                                giphy_url_list.append(
                                    {
                                        "url": item["images"]["original"]["url"],
                                        "title": item["title"]
                                    }
                                )
                        except Exception as e:
                            print(e)

        log(
            f'GIPHY: Trending List: True\n\tOffset: {offset}\n\tCount: {WebsiteData.index["api_usage"]["giphy"]["trending_limit"]}\n\tActual Length: {len(giphy_url_list)}',
            ipaddr=request.remote_addr)

        return {
            "giphy_url_list": giphy_url_list,
            "giphy_usage": giphy_usage,
            "offset": offset
        }

    def index_Picsum(request):
        picsum_url_list = []
        picsum_usage = False
        if Important.picsum_usage:
            if WebsiteData.index["api_usage"]["picsum"]["usage"]:
                picsum_usage = True
                for number in range(int(WebsiteData.index["api_usage"]["picsum"]["limit"])):
                    picsum_url_list.append(
                        str(WebsiteData.index["api_usage"]["picsum"]["api_url"]) + str(number))

        log(
            f'PICSUM: Random Images\n\tCount: {int(WebsiteData.index["api_usage"]["picsum"]["limit"])}',
            ipaddr=request.remote_addr)

        return {
            "picsum_url_list": picsum_url_list,
            "picsum_usage": picsum_usage
        }
