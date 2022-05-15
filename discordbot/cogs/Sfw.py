import discord
from discord.ext import commands
from datetime import datetime
import requests
from module import sfw
from utils import Important


class Sfw(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def giphy(self, ctx, mode, **query):

        giphy = sfw.Giphy(api_key=str(Important.giphy_api_key))

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
            value=f"Status Code:",
            inline=False
        )
        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Sfw(client))
