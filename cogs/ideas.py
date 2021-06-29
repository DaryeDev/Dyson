from discord.ext import commands
import discord
from cogs.config import config

client = discord.Client()


class Ideas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="idea",
                      brief='Da ideas a Darye para mejorar el server, los canales de Twitch y Youtube o a Dyson.')
    async def idea(self, ctx):
        guild_id = ctx.guild.id
        configData = config.load(guild_id)
        canalIdeas = configData["canales"]['canalIdeas']

        ideaMessage = ctx.message.content.replace("d.idea ", "")
        await self.bot.get_channel(int(canalIdeas)).send(
            f'@{ctx.author} dió una idea: {ideaMessage}')

    @commands.command(name="bot",
                      brief='Da ideas a Darye para mejorar a Dyson.')
    async def bot(self, ctx):
        ideaMessage = ctx.message.content.replace("d.idea ", "")
        await self.bot.get_channel(726489819517157477).send(
            f'@{ctx.author} , del servidor "{ctx.guild}" dió una idea: {ideaMessage}')


def setup(bot):
    bot.add_cog(Ideas(bot))
