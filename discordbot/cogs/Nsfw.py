import discord
import random
from discord.ext import commands
from datetime import datetime
from module import nsfw


class Nsfw(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def eporner(self, ctx, *args):

        obj = nsfw.Eporner()

        try:
            if (len(args) != 0) or (not(args is None)):
                args_str = ' '.join(args)
                images_list_first = obj.search(query=args_str, limit=50)
            else:
                images_list_first = obj.random(limit=50)
        except:
            images_list_first = obj.random(limit=50)

        video = random.choice(images_list_first)

        embed = discord.Embed(
            title=video["title"],
            url=video["src_url"],
            color=0xff0000,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )
        embed.add_field(
            name="Keywords",
            value=f'`{video["keywords"]}`',
            inline=False
        )
        embed.add_field(
            name="Views",
            value=f'`{video["views"]}`',
            inline=False
        )
        embed.add_field(
            name="Rating",
            value=f'`{video["rate"]}`',
            inline=False
        )
        embed.add_field(
            name="Uploaded on",
            value=f'`{video["uploaded_on"]}`',
            inline=False
        )
        embed.add_field(
            name="Length",
            value=f'`{video["length"]}`',
            inline=False
        )
        embed.set_image(url=str(video["url"]))
        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def redtube(self, ctx, *args):

        obj = nsfw.RedTube()

        try:
            if (len(args) != 0) or (not(args is None)):
                if args[0] in ("stars", "star", "pornstar"):
                    video = False
                    video_list = obj.stars(
                        page=str(
                            random.randint(
                                1,
                                1500
                            )
                        )
                    )
                else:
                    video = True
                    args_str = ' '.join(args)
                    video_list = obj.search(query=args_str)
            else:
                video = True
                video_list = obj.random()
        except:
            video = True
            video_list = obj.random()

        if video == True:
            video = random.choice(video_list)

            embed = discord.Embed(
                title=video["title"],
                url=video["src_url"],
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Views",
                value=f'`{video["views"]}`',
                inline=False
            )
            embed.add_field(
                name="Rating",
                value=f'`{video["rating"]}` out of `{video["ratings"]}` ratings.',
                inline=False
            )
            embed.add_field(
                name="Uploaded on",
                value=f'`{video["publish_date"]}`',
                inline=False
            )
            embed.add_field(
                name="Length",
                value=f'`{video["duration"]}`',
                inline=False
            )
            embed.set_image(url=str(video["url"]))
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            image = random.choice(video_list)

            embed = discord.Embed(
                title=image["title"],
                url=image["src_url"],
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.set_image(url=image["url"])
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Nsfw(client))
