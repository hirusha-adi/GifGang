import os
from datetime import datetime
import requests


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

