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

        image = random.choice(images_list_first)

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
        embed.add_field(
            name="Keywords",
            value=f'`{image["keywords"]}`',
            inline=False
        )
        embed.add_field(
            name="Views",
            value=f'`{image["views"]}`',
            inline=False
        )
        embed.add_field(
            name="Rating",
            value=f'`{image["rate"]}`',
            inline=False
        )
        embed.add_field(
            name="Uploaded on",
            value=f'`{image["uploaded_on"]}`',
            inline=False
        )
        embed.add_field(
            name="Length",
            value=f'`{image["length"]}`',
            inline=False
        )
        embed.set_image(url=str(image["url"]))
        embed.set_footer(text=f"Reuqested by {ctx.author.name}")
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Nsfw(client))
