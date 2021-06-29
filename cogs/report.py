from discord.ext import commands
import discord

client = discord.Client()


class Errores(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="report", brief='Reporta errores de Dyson a Darye')
    async def report(self, ctx):
        # if Error is not None:
        #     reportMessage = ctx.message.content.replace("d.report ", "")
        #     await self.bot.get_channel(748503258514980954).send(f'{ctx.author}, del canal {ctx.guild} reportó un problema: {reportMessage}')
        # else:
        #     await ctx.channel.send("¿Qué error quieres reportar?")
        #
        #     def check(m):
        #         return m.author.id == ctx.author.id
        #
        #     error = await self.bot.wait_for('message', check=check)
        #     await self.bot.get_channel(748503258514980954).send(f'{ctx.author}, del canal {ctx.guild} reportó un problema: {error}')

        reportMessage = ctx.message.content.replace("d.report ", "")
        await self.bot.get_channel(748503258514980954).send(
            f'@{ctx.author} , del servidor "{ctx.guild}" reportó un problema: {reportMessage}')


def setup(bot):
    bot.add_cog(Errores(bot))
