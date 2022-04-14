from bot.utils.filenames import database

# Users
with open(database.blacklisted_users, "r", encoding="utf-8") as _file_users:
    blacklisted_users_all_lines_first = _file_users.readlines()
    blacklisted_users_all_lines = blacklisted_users_all_lines_first


def addUser(user_id):
    if not(user_id in blacklisted_users_all_lines):
        blacklisted_users_all_lines.append(user_id)
        _updateUsersListFile()


def _updateUsersListFile():
    if not(len(blacklisted_users_all_lines_first) == len(blacklisted_users_all_lines)):
        blacklisted_users_all_lines_first = blacklisted_users_all_lines
        with open(database.blacklisted_users, "w", encoding="utf-8") as _file_users:
            for line in blacklisted_users_all_lines:
                _file_users.write(str(line))


# Guilds
with open(database.blacklisted_guilds, "r", encoding="utf-8") as _file_guilds:
    blacklisted_guilds_all_lines_first = _file_guilds.readlines()
    blacklisted_guilds_all_lines = blacklisted_guilds_all_lines_first


def addGuild(guild_id):
    if not(guild_id in blacklisted_guilds_all_lines):
        blacklisted_guilds_all_lines.append(guild_id)
        _updateGuildListFile()


def _updateGuildListFile():
    if not(len(blacklisted_guilds_all_lines_first) == len(blacklisted_guilds_all_lines)):
        blacklisted_guilds_all_lines_first = blacklisted_guilds_all_lines

        with open(database.blacklisted_guilds, "w", encoding="utf-8") as _file_guilds:
            for line in blacklisted_guilds_all_lines:
                _file_guilds.write(str(line))


# Channels
with open(database.blacklisted_channels, "r", encoding="utf-8") as _file_channels:
    blacklisted_channels_all_lines_first = _file_channels.readlines()
    blacklisted_channels_all_lines = blacklisted_channels_all_lines_first


def addChannel(channel_id):
    if not(channel_id in blacklisted_channels_all_lines):
        blacklisted_channels_all_lines.append(channel_id)
        _updateGuildListFile()


def _updateGuildListFile():
    if not(len(blacklisted_channels_all_lines_first) == len(blacklisted_channels_all_lines)):
        blacklisted_channels_all_lines_first = blacklisted_channels_all_lines

        with open(database.blacklisted_channels, "w", encoding="utf-8") as _file_channels:
            for line in blacklisted_channels_all_lines:
                _file_channels.write(str(line))
