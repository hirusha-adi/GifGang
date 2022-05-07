import json
from .filenames import FileNames

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

