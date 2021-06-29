import discord
from discord.ext import commands
from datetime import date
import asyncio
import yaml
from cogs.config import config


class calendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.checkDate(bot))
        today = date.today()
        global todayDate
        todayDate = today.strftime("%d/%m")

    async def checkDate(self, bot):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            for guild in bot.guilds:
                guild_id = guild.id
                try:
                    configData = config.load(guild_id)

                    for birthboi in configData["calendar"]["birthdays"]:
                        birthday = configData["calendar"]["birthdays"][birthboi]["date"]
                        if todayDate == birthday:
                            if configData["calendar"]["birthdays"][birthboi]["notified"] == 0:
                                channel = discord.utils.get(guild.channels, name='general')
                                birthdayMessage = str(
                                    f"🎉 @everyone, hoy es el cumpleaños de <@{birthboi}>, ¡felicidades! 🎉")
                                await channel.send(content=birthdayMessage)
                                configData["calendar"]["birthdays"][birthboi]["notified"] = 1
                                config.save(guild_id, configData)

                        else:
                            configData["calendar"]["birthdays"][birthboi]["notified"] = 0
                            config.save(guild_id, configData)
                except:
                    pass
            await asyncio.sleep(10)

    @commands.command()
    async def bday(self, ctx, dia, mes, birthboi: discord.Member = 0):
        birthboi = ctx.author if not birthboi else birthboi
        birthboi_id = birthboi.id

        if len(dia) == 1:
            dia = f"0{dia}"

        if len(mes) == 1:
            mes = f"0{mes}"

        fecha = f"{dia}/{mes}"

        guild_id = ctx.guild.id
        try:
            configData = config.load(guild_id)
        except:
            config.create(guild_id)
            configData = config.load(guild_id)

        data = "{'date': %fecha%, 'notified': 0}"
        data = data.replace("%fecha%", fecha)
        configData["calendar"]["birthdays"][birthboi_id] = yaml.safe_load(data)

        config.save(guild_id, configData)

        await ctx.send(f"Cumpleaños de {birthboi.mention} guardado como '{fecha}'")


def setup(bot):
    bot.add_cog(calendar(bot))
