import json
import os
import requests
from datetime import datetime

from utilities.vars import COUNT, COUNT_TODAY

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
    admin_settings_file = os.path.join(
        _cwd, "database", "admin", "settings.json")
    count_file = os.path.join(_cwd, "count.txt")
    count_file_today = os.path.join(_cwd, "count-today.txt")
    log_folder = os.path.join(_cwd, "logs")
    _log_file = os.path.join(log_folder, str(datetime.now())[:-7] + ".log")

    print(f"[+] Detected `config.json` at {web_server_settings}")
    print(f"[+] Detected `settings.json` at {important_info_file}")
    print(f"[+] Detected `website.json` at {website_info_file}")
    print(f"[+] Detected `login/admin.json` at {admin_settings_file}")
    print(f"[+] Detected Logs at {log_folder}")
    print(f'Visit count file will be at {count_file}')
    print(f'Visit count file per day will be at {count_file_today}')


class Settings:
    class Admin:
        with open(FileNames.admin_settings_file, "r", encoding="utf-8") as _admin_file:
            _admin_data = json.load(_admin_file)

        # Main
        # --------------------------------------
        username = _admin_data["username"]
        password = _admin_data["password"]
        token = _admin_data["token"]
        profile_pic = _admin_data["profile_pic"]

        # Others
        # --------------------------------------
        _targets = _admin_data["targets"]
        targets_today = _targets["today"]
        targets_all = _targets["all"]


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


def logf(request, page: str):
    if not(os.path.exists(FileNames._log_file)):
        with open(FileNames._log_file, "w", encoding="utf-8") as filem:
            filem.write(
                f"[{datetime.now()}] - 'Created the log file!' ")

    with open(FileNames._log_file, "a+", encoding="utf-8") as file:
        file.write(
            f'\n[{datetime.now()}] ({request.remote_addr}) - /{page} - \"{request.user_agent}\"')


def count_total_visits_amount():
    global COUNT, COUNT_TODAY

    # Main
    if not(os.path.isfile(FileNames.count_file)):
        with open(FileNames.count_file, "w", encoding="utf-8") as f_make_no_exist:
            if COUNT is None:
                f_make_no_exist.write("1")
            else:
                f_make_no_exist.write(str(int(COUNT)))

    with open(FileNames.count_file, "r", encoding="utf-8") as f_read:
        current_count = f_read.read()

    try:
        current_count = int(current_count)
        COUNT = current_count
    except ValueError:
        current_count = COUNT

    with open(FileNames.count_file, "r", encoding="utf-8") as f_read:
        current_count = f_read.read()

    with open(FileNames.count_file, "w", encoding="utf-8") as f_write:
        new_count = COUNT + 1
        f_write.write(str(new_count))

    # Daily
    if not(os.path.isfile(FileNames.count_file_today)):
        with open(FileNames.count_file_today, "w", encoding="utf-8") as f_make_no_exist_tdy:
            if COUNT_TODAY is None:
                f_make_no_exist_tdy.write("1")
            else:
                f_make_no_exist_tdy.write(str(int(COUNT_TODAY)))

    with open(FileNames.count_file_today, "r", encoding="utf-8") as fd_read:
        current_count_daily = fd_read.read()

    try:
        current_count_daily = int(current_count_daily)
        COUNT_TODAY = current_count_daily
    except ValueError:
        current_count_daily = COUNT_TODAY

    with open(FileNames.count_file_today, "r", encoding="utf-8") as fd_read:
        current_count_daily = fd_read.read()

    with open(FileNames.count_file_today, "w", encoding="utf-8") as fd_write:
        new_count_daily = COUNT_TODAY + 1
        fd_write.write(str(new_count_daily))
