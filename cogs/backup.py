import discord
from discord import guild
from discord.ext import commands
import requests
import asyncio
import os
import datetime
import yaml

class backup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['backup'])
    async def bak(self, ctx):
        if ctx.author.id == 439470338150236162:
            for guild in self.bot.guilds:
                now = datetime.datetime.now()
                guild_id = guild.id
                base_dir = 'config'
                bakDir = 'backup'
                guildDir = f"{guild.name} ({guild.id})"
                guildPath = os.path.join(bakDir, guildDir)
                configName = str(guild_id) + '.yml'
                bakName = f"{str(guild_id)}({now}).yml.bak"
                configFile = open(os.path.join(base_dir, configName), 'r')
                configPath = os.path.join(base_dir, configName)
                bakPath = os.path.join(guildPath, bakName)
                configData = yaml.safe_load(configFile)
                try:
                    os.mkdir(guildPath)
                except:
                    pass
                with open(bakPath, "w") as f:
                    yaml.dump(configData, f)
                    print(f"¡Copia de seguridad de {guild} realizada!")
            await ctx.channel.send("¡Copia de seguridad realizada!")


def setup(bot):
    bot.add_cog(backup(bot))
