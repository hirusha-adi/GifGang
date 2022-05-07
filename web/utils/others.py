import os
from datetime import datetime

from .filenames import FileNames
from .config import Config

from utils.vars import COUNT, COUNT_TODAY

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
