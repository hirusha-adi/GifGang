import os
import platform
from datetime import datetime

import discord
import requests
from discord.ext import commands


class CatAAS(commands.Cog):
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
    async def gif(self, ctx, *, text=None):
        if text is None:
            final_url = "https://cataas.com/cat/gif"
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
            await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx, *, text=None):
        if text is None:
            final_url = "https://cataas.com/cat"
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
            await ctx.send(embed=embed)

    @commands.command()
    async def filter(self, ctx, filter_name="sepia", *, text=None):
        """
        filter_name: str --> 
            Defaults to "sepia"
            Available Values:
                blur, mono, sepia, negative, paint, pixel
        """
        if text is None:
            final_url = f"https://cataas.com/cat?filter={filter_name}"
        else:
            final_url = f"https://cataas.com/cat/says/{text}?filter={filter_name}"

        if self.saveImage(url=final_url):
            file = discord.File(f'temp.png', filename="temp.png")
            embed = discord.Embed(title="a Cat",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_image(url="attachment://temp.png")
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
            await ctx.send(embed=embed)

    @commands.command(aliases=["filter-gif", "filterg"])
    async def filtergif(self, ctx, filter_name="sepia", *, text=None):
        """
        filter_name: str --> 
            Defaults to "sepia"
            Available Values:
                blur, mono, sepia, negative, paint, pixel
        """
        if text is None:
            final_url = f"https://cataas.com/cat/gif?filter={filter_name}"
        else:
            final_url = f"https://cataas.com/cat/gif/says/{text}?filter={filter_name}"

        if self.saveGIF(url=final_url):
            file = discord.File(f'temp.gif', filename="temp.gif")
            embed = discord.Embed(title="a Cat",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_image(url="attachment://temp.gif")
            await ctx.send(file=file, embed=embed)

            self.removeImage(filename="temp.gif")

        else:
            embed = discord.Embed(title="An Error has Occured",
                                  description="Unable to load the Image from the API",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(CatAAS(client))
