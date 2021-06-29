import json
import pprint
import urllib

import discord
import requests
from discord.ext import commands
from discord.ext.commands import bot


class Musica(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def urlGif(accion):
        apikey = "pito"  # test value
        lmt = 1
        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (accion, apikey, lmt))

        if r.status_code == 200:
            pp = pprint.PrettyPrinter(indent=4)
            gif = json.loads(r.content)
            for i in range(len(gif['results'])):
                url = gif['results'][i]['media'][0]['gif']['url']

    @commands.command(name='abrazar', aliases=['hug', 'abrazo'],
                      brief='Abraza a tu compañero uwu')
    async def abrazar(self, ctx):
        """Abraza a tu compañero uwu."""
        actionUser = discord.message.content.replace("d.abrazar ", "")
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        embed.add_field(name="‎", value="**"+discord.message.author+ "** abrazó a **"+actionUser+"**. uwu")
        self.urlGif("hug")
        embed.set_image(url=self.url)
        await bot.say(embed=embed)

def setup(bot):
    bot.add_cog(respuestas(bot))
