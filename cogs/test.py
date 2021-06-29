import json
import pprint
import urllib

import discord
import requests
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test',
                      brief='Abraza a tu compañero uwu')
    async def test(self, ctx):
        userIcon = ctx.author.avatar_url
        print (userIcon)

        img_data = requests.get(userIcon).content
        with open('userIcon.png', 'wb') as handler:
                handler.write(img_data)

def setup(bot):
    bot.add_cog(test(bot))