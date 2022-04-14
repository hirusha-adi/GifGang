import json
from bot.utils.filenames import database


with open(database.main, "r", encoding="utf-8") as _file:
    data = json.load(_file)

prefix = data['prefix']
token = data['token']
admins = data['admins']
