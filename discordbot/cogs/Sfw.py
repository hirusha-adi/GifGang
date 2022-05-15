import discord
import random
import os
from discord.ext import commands
from datetime import datetime
import requests
from module import sfw
from utils import Important


class Sfw(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    def saveImage(self, url: str):
        try:
            r = requests.get(url)
            with open("temp.png", "wb") as fimg:
                fimg.write(r.content)
            return True
        except:
            return False

    def saveGIF(self, url: str):
        try:
            r = requests.get(url).content
            with open("temp.gif", "wb") as fimg:
                fimg.write(r)
            return True
        except:
            return False

    def removeImage(self, filename: str = "temp.png"):
        os.system("rm -rf ./{delfname}".format(delfname=filename))

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
    async def tenor(self, ctx, *query):

        random_search_words = (
            "animal", "cat", "dog", "anime", "wallpaper", "scenery", "mountains", "happy", "office",
            "perception", "youth", "variety", "refrigerator", "government", "performance", "marriage", "responsibility",
            "loss", "success", "profession", "feedback", "housing", "chapter", "editor", "bird", "climate", "wife",
            "presence", "health", "meal", "customer", "dirt", "idea", "satisfaction", "imagination", "employment", "indication",
            "politics", "anxiety", "manager", "movie", "person", "unit", "session", "temperature", "poem", "construction",
            "relationship", "departure", "instance", "week", "ratio", "application", "complaint", "activity", "story", "lady",
            "administration", "psychology",
        )
        tenor = sfw.Tenor(api_key=str(Important.tenor_api_key))

        if len(query) >= 1:
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

    @commands.command()
    async def cataas(self, ctx, mode=None, *text):
        image_words = ["img", "i", "image"]
        if mode is None:
            mode = "gif"

        try:
            if len(text) == 0:
                text = None
        except:
            text = None

        all_filters = ("blur", "mono", "sepia", "negative", "paint", "pixel")

        if not(mode in image_words):  # GIF
            if text is None:
                final_url = "https://cataas.com/cat/gif"
            else:
                text = ' '.join(text)
                filter_name = text.split(" ")[-1]

                if text.split(" ")[-1] in all_filters:
                    processed_text = ' '.join(text.split(" ")[:-1])
                    final_url = f"https://cataas.com/cat/gif/says/{processed_text}?filter={filter_name}"
                else:
                    final_url = f"https://cataas.com/cat/gif/says/{text}"

            if self.saveGIF(url=final_url):
                file = discord.File(f'temp.gif', filename="temp.gif")
                embed = discord.Embed(title="a Cat",
                                      color=0xcb42f5,
                                      timestamp=datetime.utcnow())
                embed.set_author(name=str(self.client.user.name),
                                 icon_url=str(self.client.user.avatar_url))
                embed.set_image(url="attachment://temp.gif")
                embed.set_footer(
                    text=f"CatAAS - Reuqested by {ctx.author.name}")
                await ctx.send(file=file, embed=embed)

                self.removeImage(filename="temp.gif")

            else:
                embed = discord.Embed(title="An Error has Occured",
                                      description="Unable to load the GIF from the API",
                                      color=0xcb42f5,
                                      timestamp=datetime.utcnow())
                embed.set_author(name=str(self.client.user.name),
                                 icon_url=str(self.client.user.avatar_url))
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed.set_footer(
                    text=f"CatAAS - Reuqested by {ctx.author.name}")
                await ctx.send(embed=embed)

        else:  # Images
            if text is None:
                final_url = "https://cataas.com/cat"
            else:
                text = ' '.join(text)
                filter_name = text.split(" ")[-1]
                if text.split(" ")[-1] in all_filters:
                    processed_text = ' '.join(text.split(" ")[:-1])
                    final_url = f"https://cataas.com/cat/says/{processed_text}?filter={filter_name}"
                else:
                    final_url = f"https://cataas.com/cat/says/{text}"

            if self.saveImage(url=final_url):
                file = discord.File(f'temp.png', filename="temp.png")
                embed = discord.Embed(title="a Cat",
                                      color=0xcb42f5,
                                      timestamp=datetime.utcnow())
                embed.set_author(name=str(self.client.user.name),
                                 icon_url=str(self.client.user.avatar_url))
                embed.set_image(url="attachment://temp.png")
                embed.set_footer(
                    text=f"CatAAS - Reuqested by {ctx.author.name}")
                await ctx.send(file=file, embed=embed)

                self.removeImage(filename="temp.png")

            else:
                embed = discord.Embed(title="An Error has Occured",
                                      description="Unable to load the Image from the API",
                                      color=0xcb42f5,
                                      timestamp=datetime.utcnow())
                embed.set_author(name=str(self.client.user.name),
                                 icon_url=str(self.client.user.avatar_url))
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed.set_footer(
                    text=f"CatAAS - Reuqested by {ctx.author.name}")
                await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Sfw(client))
