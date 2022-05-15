import discord
import random
from discord.ext import commands
from datetime import datetime
import requests
from module import sfw
from utils import Important


class Sfw(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def giphy(self, ctx, mode=None, *query):

        all_modes = ("random", "trending", "search")
        if mode is None:
            mode = "random"
        else:
            if not(mode in all_modes):
                mode = "random"

        giphy = sfw.Giphy(api_key=str(Important.giphy_api_key))

        if mode == "trending":
            images_list = giphy.trending(limit=1)
        elif mode == "search":
            images_list = giphy.search(query=' '.join(query), limit=1)
        else:
            images_list = giphy.random(limit=1)

        for image in images_list:
            embed = discord.Embed(
                title=image['title'],
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.set_image(url=str(image['url']))
            embed.set_footer(text=f"GIPHY - Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)

        del(giphy)

    @commands.command()
    async def picsum(self, ctx):

        picsum = sfw.Picsum()
        images_list = picsum.images(limit=120, height=500, width=200)

        embed = discord.Embed(
            title="",
            color=0xff0000,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )
        embed.set_image(url=images_list[random.randint(0, len(images_list)-1)])
        embed.set_footer(text=f"PICSUM - Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)

        del(picsum)

    @commands.command()
    async def tenor(self, ctx, mode=None, *query):
        random_search_words = (
            "animal", "cat", "dog", "anime", "wallpaper", "scenery", "mountains", "happy", "office"
        )
        all_modes = ("random", "search")
        if mode is None:
            mode = "random"
        else:
            if not(mode in all_modes):
                mode = "random"

        tenor = sfw.Tenor(api_key=str(Important.tenor_api_key))

        if mode == "search":
            images_list = tenor.search(
                query=' '.join(query),
                limit=1
            )
        else:
            images_list = tenor.search(
                query=random.choice(random_search_words),
                limit=1
            )

        for image in images_list:
            embed = discord.Embed(
                title=image['title'],
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.set_image(url=str(image['url']))
            embed.set_footer(text=f"TENOR - Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Sfw(client))
