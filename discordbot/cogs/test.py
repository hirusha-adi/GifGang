import os
import platform
from datetime import datetime

import aiohttp
import discord
import requests
import random
from discord.ext import commands


class TheCat(commands.Cog):
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
    async def breed(self, ctx):
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
                    embed.set_footer(text=EmbedsDB.common["footer"].format(
                        author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
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
                    embed.set_footer(text=EmbedsDB.common["footer"].format(
                        author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
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
        embed.set_footer(text=EmbedsDB.common["footer"].format(
            author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
        await ctx.send(embed=embed)

    @commands.command()
    async def cats(self, ctx, *, count=None):
        max_possible = int(EmbedsDB.commands["cats"]["max_amount"])
        count_error = False

        if count is None:
            count = 1
        else:
            try:
                count = int(count)
            except TypeError:
                count = 1
                count_error = True

        if count > max_possible:
            embed = discord.Embed(title="An Error has Occured",
                                  description=f"Please enter value below {max_possible} to prevent scams",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed)

        #       https://api.thecatapi.com/v1/images/search?limit=3
        url = f"https://api.thecatapi.com/v1/images/search?limit={count}"

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
                    embed.set_footer(text=EmbedsDB.common["footer"].format(
                        author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
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
                    embed.set_footer(text=EmbedsDB.common["footer"].format(
                        author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
                    await ctx.send(embed=embed)

        iter = 1
        for one_image in result:
            if count_error:
                embed = discord.Embed(title=f"a Cat - {iter}",
                                      description="Defaulted to one image. Please refer to the command usage for additonal information",
                                      color=0xcb42f5,
                                      timestamp=datetime.utcnow())
            else:
                embed = discord.Embed(title=f"a Cat - {iter}",
                                      color=0xcb42f5,
                                      timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_image(url=f"{one_image['url']}")
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed)
            iter += 1


def setup(client: commands.Bot):
    client.add_cog(TheCat(client))
