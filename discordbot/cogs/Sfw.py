import os
import random
from datetime import datetime

import aiohttp
import discord
import requests
from discord.ext import commands
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

        """
        Usage:
            .giphy [mode] [query]

        Arguments:
            [mode]
                "trending" / "search" / "random"
                defaults to "random"

            [query]
                only needed if [mode] is "search"

        Examples:
            .giphy                          | works
            .giphy search happy birthday    | works
            .giphy trending                 | works

            .giphy search                   | defaults to "random"
        """

        all_modes = ("random", "trending", "search")
        if mode is None:
            mode = "random"
        else:
            if not(mode in all_modes):
                mode = "random"

        giphy = sfw.Giphy(api_key=str(Important.giphy_api_key))

        try:
            if mode == "trending":
                images_list = giphy.trending(limit=1)
            elif mode == "search":
                images_list = giphy.search(query=' '.join(query[1:]), limit=1)
            else:
                images_list = giphy.random(limit=1)
        except IndexError:
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

    @commands.command()
    async def thecatapi(self, ctx, mode=None):
        if mode is None:
            mode = "image"

        if mode.lower() in ("b", "breed"):
            url = "https://api.thecatapi.com/v1/breeds"

            async with aiohttp.ClientSession() as catSession:
                async with catSession.get(url) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed = discord.Embed(title="An Error has Occured",
                                              description="Bad status code from API",
                                              color=0xcb42f5,
                                              timestamp=datetime.utcnow())
                        embed.set_author(name=str(self.client.user.name),
                                         icon_url=str(self.client.user.avatar_url))
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed.set_footer(
                            text=f"TheCatAPI - Reuqested by {ctx.author.name}")
                        await ctx.send(embed=embed)

                    try:
                        result = await jsondata.json()
                    except Exception as e:
                        embed = discord.Embed(title="An Error has Occured",
                                              description=f"Unable to convert fetched data to JSON from API: {e}",
                                              color=0xcb42f5,
                                              timestamp=datetime.utcnow())
                        embed.set_author(name=str(self.client.user.name),
                                         icon_url=str(self.client.user.avatar_url))
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed.set_footer(
                            text=f"TheCatAPI - Reuqested by {ctx.author.name}")
                        await ctx.send(embed=embed)

            data = result[random.randint(1, len(result) - 1)]

            final_Links = ""
            try:
                final_Links += f"CFA: {data['cfa_url']}\n"
            except:
                pass
            try:
                final_Links += f"VetStreet: {data['vetstreet_url']}\n"
            except:
                pass
            try:
                final_Links += f"VCA Hospitals: {data['vcahospitals_url']}"
            except:
                pass

            final_CountryOfOrigin = ""
            try:
                final_CountryOfOrigin += f"Origin: {data['origin']}\n"
            except:
                pass
            try:
                final_CountryOfOrigin += f"Country Code: {data['country_code']}"
            except:
                pass

            final_Stats = ""
            try:
                final_Stats += f"Indoor: {data['indoor']}\n"
            except:
                pass
            try:
                final_Stats += f"Lap: {data['lap']}\n"
            except:
                pass
            try:
                final_Stats += f"Adaptability: {data['adaptability']}\n"
            except:
                pass
            try:
                final_Stats += f"Affection Level: {data['affection_level']}\n"
            except:
                pass
            try:
                final_Stats += f"Child Friendly: {data['child_friendly']}\n"
            except:
                pass
            try:
                final_Stats += f"Dog Friendly: {data['dog_friendly']}\n"
            except:
                pass
            try:
                final_Stats += f"Energy Level: {data['energy_level']}\n"
            except:
                pass
            try:
                final_Stats += f"Grooming: {data['grooming']}"
            except:
                pass

            try:
                final_Stats += f"Health Issues: {data['health_issues']}\n"
            except:
                pass
            try:
                final_Stats += f"Intelligence: {data['intelligence']}\n"
            except:
                pass
            try:
                final_Stats += f"Shedding Level: {data['shedding_level']}\n"
            except:
                pass
            try:
                final_Stats += f"Social Needs: {data['social_needs']}\n"
            except:
                pass
            try:
                final_Stats += f"Stranger Friendly: {data['stranger_friendly']}\n"
            except:
                pass
            try:
                final_Stats += f"Vocalisation: {data['vocalisation']}\n"
            except:
                pass
            try:
                final_Stats += f"Experimental: {data['experimental']}\n"
            except:
                pass
            try:
                final_Stats += f"Hairless: {data['hairless']}\n"
            except:
                pass
            try:
                final_Stats += f"Natural: {data['natural']}\n"
            except:
                pass
            try:
                final_Stats += f"Rare: {data['rare']}\n"
            except:
                pass
            try:
                final_Stats += f"Rex: {data['rex']}\n"
            except:
                pass
            try:
                final_Stats += f"Suppressed Tail: {data['suppressed_tail']}\n"
            except:
                pass
            try:
                final_Stats += f"Short Legs: {data['short_legs']}\n"
            except:
                pass
            try:
                final_Stats += f"Hyperallergenic: {data['hypoallergenic']}"
            except:
                pass

            embed = discord.Embed(title=f"{data['name']}",
                                  description=f"{data['description']}",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_image(url=f"{data['image']['url']}")
            embed.add_field(name="Links",
                            value=final_Links,
                            inline=False)
            embed.add_field(name="Wikipedia",
                            value=f"{data['wikipedia_url']}",
                            inline=False)
            embed.add_field(name="Temperament",
                            value=f"{data['temperament']}",
                            inline=False)
            embed.add_field(name="Country Of Origin",
                            value=final_CountryOfOrigin,
                            inline=False)
            embed.add_field(name="Lifespan",
                            value=f"{data['life_span']}",
                            inline=False)
            embed.add_field(name="Stats",
                            value=final_Stats,
                            inline=False)
            embed.set_footer(
                text=f"TheCatAPI - Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            url = f"https://api.thecatapi.com/v1/images/search?limit=1"

            async with aiohttp.ClientSession() as catSession:
                async with catSession.get(url) as jsondata:
                    if not 300 > jsondata.status >= 200:
                        embed = discord.Embed(title="An Error has Occured",
                                              description="Bad status code from API",
                                              color=0xcb42f5,
                                              timestamp=datetime.utcnow())
                        embed.set_author(name=str(self.client.user.name),
                                         icon_url=str(self.client.user.avatar_url))
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed.set_footer(
                            text=f"TheCatAPI - Reuqested by {ctx.author.name}")
                        await ctx.send(embed=embed)
                        return

                    try:
                        result = await jsondata.json()
                    except Exception as e:
                        embed = discord.Embed(title="An Error has Occured",
                                              description=f"Unable to convert fetched data to JSON from API: {e}",
                                              color=0xcb42f5,
                                              timestamp=datetime.utcnow())
                        embed.set_author(name=str(self.client.user.name),
                                         icon_url=str(self.client.user.avatar_url))
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed.set_footer(
                            text=f"TheCatAPI - Reuqested by {ctx.author.name}")
                        await ctx.send(embed=embed)
                        return

            for one_image in result:
                embed = discord.Embed(title=f"a Cat",
                                      color=0xcb42f5,
                                      timestamp=datetime.utcnow())
                embed.set_author(name=str(self.client.user.name),
                                 icon_url=str(self.client.user.avatar_url))
                embed.set_image(url=f"{one_image['url']}")
                embed.set_footer(
                    text=f"TheCatAPI - Reuqested by {ctx.author.name}")
                await ctx.send(embed=embed)

    @commands.command()
    async def dogs(self, ctx):

        dogs = sfw.Dogs()
        images_list = dogs.images(limit=1)

        for image in images_list:
            embed = discord.Embed(
                title="a Dog",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.set_image(url=str(image))
            embed.set_footer(text=f"GIPHY - Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Sfw(client))
