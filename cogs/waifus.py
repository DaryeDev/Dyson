from discord import message, guild
import discord
from discord.ext import commands
from discord import Guild
import asyncio
import os
import yaml

class waifus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def w(self, ctx):
        pass

    @commands.command()
    async def wlist(self, ctx):
        pass

    @commands.command()
    async def wadd(self, ctx):
        pass

def setup(bot):
    bot.add_cog(waifus(bot))