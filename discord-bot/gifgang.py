import os

import discord
from discord.ext import commands

from src.db import Config
from src.utils import Filenames

with open(Filenames.token_txt, "r", encoding="utf-8") as _token_file:
    TOKEN = _token_file.read()

client = commands.Bot(command_prefix=Config.prefix)

for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'src.cogs.{filename[:-3]}')
            print(f"[+] Loaded: src.cogs.{filename[:-3]}")
        except Exception as excl:
            print(
                f"[+] Unable to load: src.cogs.{filename[:-3]}  :  {excl}")


@client.command()
async def loadex(ctx, extension):
    if ctx.author.id in Config.admins:
        client.load_extension(
            f'src.cogs.{extension if not(str(extension).endswith(".py")) else extension[:-3]}')
        await ctx.send(f"Loaded cog: {extension}")
    else:
        await ctx.send("You do not have permissions to use this command!")


@client.command()
async def unloadex(ctx, extension):
    if ctx.author.id in Config.admins:
        client.unload_extension(
            f'src.cogs.{extension if not(str(extension).endswith(".py")) else extension[:-3]}')
        await ctx.send(f"Un-Loaded cog: {extension}")
    else:
        await ctx.send("You do not have permissions to use this command!")


client.run(TOKEN)
