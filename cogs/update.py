import discord
from discord import guild
from discord.ext import commands
import requests
import asyncio
import os
from datetime import date
import yaml
import subprocess


class update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['upd'])
    async def update(self, ctx, module=None):
        if ctx.author.id == 439470338150236162:
            if module != None:
                process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
                output = process.communicate()[0]
                try:
                    self.bot.reload_extension(f"cogs.{module}")
                    await ctx.channel.send(f"¡Módulo {module} actualizado!")
                except:
                    await ctx.channel.send("Módulo no encontrado, comprueba que está bien escrito y vuélvelo a intentar :'c")

            else:
                process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
                output = process.communicate()[0]
                with open("cogs.yaml", "r") as f:
                    cogList = yaml.safe_load(f)
                for cog in cogList["cogs"]:
                    if cogList["cogs"][cog]["enabled"]:
                        self.bot.reload_extension(f"cogs.{cog}")
                await ctx.channel.send("¡Todos los módulos actualizados!")
        else:
            pass

def setup(bot):
    bot.add_cog(update(bot))
