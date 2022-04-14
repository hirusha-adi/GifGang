import os

_cwd = os.getcwd()
_database = os.path.join(_cwd, "bot", "database")


main = os.path.join(
    _database,
    "data",
    "main.json"
)

blacklisted_users = os.path.join(
    _database,
    "data",
    "blacklisted_users.txt"
)

blacklisted_guilds = os.path.join(
    _database,
    "data",
    "blacklisted_guilds.txt"
)

blacklisted_channels = os.path.join(
    _database,
    "data",
    "blacklisted_channels.txt"
)
