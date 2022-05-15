import discord
from discord.ext import commands
import time
from datetime import datetime


class Base(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.start_time = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("="*50)
        print(f'[*] Logged in as {self.client.user.name}')
        print(f'[*] Discord.py API Version: {discord.__version__}')
        print('[+] Bot is ready to be used!')
        print("="*50)
        await self.client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name='GifGang.net'
            )
        )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        embed = discord.Embed(
            title="An error has occured",
            color=0xff0000,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/961984775176982558/unknown.png?size=4096")

        if isinstance(error, commands.MissingAnyRole):
            embed.add_field(
                name="Error:",
                value="User Missing Any Role.",
                inline=False
            )

        if isinstance(error, commands.MissingPermissions):
            embed.add_field(
                name="Error:",
                value="User Missing Permissions to use this command.",
                inline=False
            )

        if isinstance(error, commands.MissingRequiredArgument):
            embed.add_field(
                name="Error:",
                value="Missing Required Argument. Not all arguments for the usage of this command was passed. Please refer help.",
                inline=False
            )

        if isinstance(error, commands.MissingRole):
            embed.add_field(
                name="Error:",
                value="User Missing Role. You dont have a required role to use this command.",
                inline=False
            )

        if isinstance(error, commands.BotMissingAnyRole):
            embed.add_field(
                name="Error:",
                value=f"Bot Missing Role. {self.client.user.name} does not have any role for this.",
                inline=False
            )

        if isinstance(error, commands.BotMissingPermissions):
            embed.add_field(
                name="Error:",
                value=f"Bot Missing Permissions. {self.client.user.name} does not have enough permission for this command to be run successfully.",
                inline=False
            )

        if isinstance(error, commands.BotMissingRole):
            embed.add_field(
                name="Error:",
                value=f"Bot Missing Role. {self.client.user.name} does not have a required role to complete this action.",
                inline=False
            )

        if isinstance(error, commands.ArgumentParsingError):
            embed.add_field(
                name="Error:",
                value=f"Unable to process the arguments given with the command",
                inline=False
            )

        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Pong!",
            color=0xff0000,
            description=f"That took you: `{round(self.client.latency * 1000)} ms`",
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )
        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Base(client))
