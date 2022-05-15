import discord
from discord.ext import commands
from datetime import datetime
import urllib.request


class Base(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

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
            value=f"Status Code:",
            inline=False
        )
        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Base(client))
