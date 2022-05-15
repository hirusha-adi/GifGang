import discord
from discord.ext import commands
import time
from datetime import datetime
from datetime import timedelta
import urllib.request


class Base(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.start_time = None

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


def setup(client: commands.Bot):
    client.add_cog(Base(client))
