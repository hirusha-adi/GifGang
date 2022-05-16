import time
import urllib.request
from datetime import datetime, timedelta

import discord
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.start_time = None

        self.client.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print("="*50)
        print(f'[*] Logged in as {self.client.user.name}')
        print(f'[*] Discord.py API Version: {discord.__version__}')
        print('[+] Bot is ready to be used!')
        print("="*50)
        self.start_time = time.time()
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
            title=f"Pong!\nThat took you: `{round(self.client.latency * 1000)} ms`",
            color=0xff0000,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )
        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def uptime(self, ctx):
        embed = discord.Embed(
            title=f"Uptime",
            color=0xff0000,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )
        embed.add_field(
            name="Website",
            value=f"Status Code: `{urllib.request.urlopen('https://gifgang.net').getcode()}`",
            inline=False
        )
        current_time = time.time()
        difference = int(round(current_time - self.start_time))
        text = str(timedelta(seconds=difference))
        embed.add_field(
            name="Discord Bot",
            value=f"Running for `{text}`",
            inline=False
        )
        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx, cmnd=None):
        if cmnd == "giphy":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot | Giphy",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.giphy [mode] [query]```",
                inline=False
            )
            embed.add_field(
                name="Arguments:",
                value=f'**[mode]**\n`"trending" / "search" / "random"`\n`defaults to "random"`\n**[query]**\n`only needed if [mode] is "search"`',
                inline=False
            )
            embed.add_field(
                name="Examples:",
                value=f"`.giphy                          | works`\n`.giphy search happy birthday    | works`\n`.giphy trending                 | works`\n`.giphy search                   | defaults to 'random'`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "picsum":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot | Picsum",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.thecatapi```",
                inline=False
            )
            embed.add_field(
                name="Examples:",
                value=f"`.picsum`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "cataas":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot | Cat As A Service",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.cataas [mode] [text] [filter]```",
                inline=False
            )
            embed.add_field(
                name="Arguments:",
                value=f'**[mode]**\n`"img" / "i" / "image" / "gif"`\n**[text]**\n`any text to add on top of the image`\n`if there is no text, this can be replaced with [filter]`\n**[filter]**\n`"blur" / "mono" / "sepia" / "negative" / "paint" / "pixel"`\n`filter name`\n`defaults to None`',
                inline=False
            )
            embed.add_field(
                name="Examples:",
                value=f"`.cataas gif                     | works`\n`.cataas img                     | works`\n`.cataas img hey Babe?           | works`\n`.cataas img Hey babe? sepia     | works`\n`.cataas img sepia               | works`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "tenor":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot | Tenor",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.tenor [query]```",
                inline=False
            )
            embed.add_field(
                name="Arguments:",
                value=f'**[query]**\n`what to search for.`\n`defaults to a randomly selected word`',
                inline=False
            )
            embed.add_field(
                name="Examples:",
                value=f"`.tenor                  | works`\n`.tenor good morning     | works`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "thecatapi":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot | The Cat API",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.thecatapi [mode]```",
                inline=False
            )
            embed.add_field(
                name="Arguments:",
                value=f'**[mode]**\n`"b" / "breed" / "i" / "img" / "image"`\n`defaults to "image"`',
                inline=False
            )
            embed.add_field(
                name="Examples:",
                value=f"`.thecatapi          | works`\n`.thecatapi image    | works`\n`.thecatapi b        | works`\n`.thecatapi breed    | works`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "erporner":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot | Eporner",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.erporner [query]```",
                inline=False
            )
            embed.add_field(
                name="Arguments:",
                value=f'**[query]**\n`what to search for`\n`defaults to a randomly selected word`',
                inline=False
            )
            embed.add_field(
                name="Examples:",
                value=f"`.eporner            | works`\n`.eporner cumshot    | works`\n`.eporner lesbians   | works`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "redtube":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot | RedTube",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.redtube [mode-or-query]```",
                inline=False
            )
            embed.add_field(
                name="Arguments:",
                value=f'**[mode-or-query]**\n`"stars", "star", "pornstar"`\n`if first word is in above words,`\n\t`will send a random pornstar`\n`if not,`\n\t`will search for result in redtube`\n`this can be the mode or what to search for`',
                inline=False
            )
            embed.add_field(
                name="Examples:",
                value=f"`.redtube            | works`\n`.redtube star       | works - send random pornstar`\n`.redtube cumshot    | works`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "ping":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow(),
                description="Send the reponse time of GifGang's Discord Bot"
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.ping```",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "uptime":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow(),
                description="Send the uptime of GifGang"
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.uptime```",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        elif cmnd == "about":
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot",
                url="https://gifgang.net/discord/help",
                color=0xff0000,
                timestamp=datetime.utcnow(),
                description="Send information about GifGang"
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Usage:",
                value=f"```.about```",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f"Help for GifGang's Discord Bot",
                url="https://gifgang.net/discord/help",
                description="you can run `.help [name]` for additional information",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="General",
                value=f"`ping`\n`uptime`\n`about`",
                inline=False
            )
            embed.add_field(
                name="SFW Commands",
                value=f"`giphy [mode] [query]`\n`picsum`\n`tenor [query]`\n`cataas [mode] [text] [filter]`\n`thecatapi [mode]`",
                inline=False
            )
            embed.add_field(
                name="SFW Commands",
                value=f"`erporner [query]`\n`redtube [mode-or-query]`",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Base(client))
