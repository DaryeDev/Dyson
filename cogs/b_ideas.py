# Muy mal hecho, no usar.


from discord.ext import commands
import discord
from cogs.config import config
import os
import yaml

client = discord.Client()


class b_Ideas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="idea",
                      brief='Da ideas a Darye para mejorar el server, los canales de Twitch y Youtube o a Dyson.')
    async def idea(self, ctx, modo):
        guild_id = ctx.guild.id
        configData = config.load(guild_id)

        base_dir = 'config'
        g_configName = 'global.yml'
        print(os.path.join(base_dir, g_configName))
        g_configFile = open(os.path.join(base_dir, g_configName), 'w+')
        g_configData = yaml.safe_load(g_configFile)

        canalIdeas = f"""{configData["canales"]['canalIdeas']}"""
        ideasNo = g_configData["ideas"]["ideasNo"]

        if modo == "add":
            idea = ctx.message.content.replace("d.idea add ", "")
            await self.bot.get_channel(int(canalIdeas)).send(
                f'[Idea No. {ideasNo + 1}] <@{ctx.author.id}> dió una idea: {idea}')
            configData['ideas'][ideasNo + 1]["idea"] = idea
            configData['ideas'][ideasNo + 1]["author"] = ctx.author.id
            configData['ideas'][ideasNo + 1]["votes"] = int("0")
            await ctx.channel.send(
                f"""Gracias por la idea, <@{ctx.author.id}! La tendremos en consideración! Puedes ver su estado poniendo "d.idea info" y tu codigo de Idea, que es el *{ideasNo + 1}* """)
            configData['ideas'][ideasNo] = int(ideasNo + 1)

        if modo == "info":
            ideaNo = ctx.message.content.replace("d.idea info ", "")

            idea = configData['ideas'][ideaNo]["idea"]
            ideaAuthor = configData['ideas'][ideaNo]["author"]
            ideaVotes = configData['ideas'][ideaNo]["votes"]

            await self.bot.get_channel(int(canalIdeas)).send(
                f'[Idea No. {ideaNo}] <@{ideaAuthor}> dió una idea y tiene {ideaVotes} votos: "{idea}"')

        if modo == "vote":
            ideaNo = ctx.message.content.replace("d.idea vote ", "")

            idea = configData['ideas'][ideaNo]["idea"]
            ideaAuthor = configData['ideas'][ideaNo]["author"]
            ideaVotes = (configData['ideas'][ideaNo]["votes"] + 1)

            await self.bot.get_channel(int(canalIdeas)).send(
                f'[Idea No. {ideaNo}] Has votado por la idea de <@{ideaAuthor}> y ahora tiene {ideaVotes} votos: "{idea}"')

            configData['ideas'][ideasNo]["votes"] = ideaVotes

    @commands.command(name="bot",
                      brief='Da ideas a Darye para mejorar a Dyson.')
    async def bot(self, ctx):

        ideaMessage = ctx.message.content.replace("d.idea ", "")
        await self.bot.get_channel(726489819517157477).send(
            f'@{ctx.author} , del servidor "{ctx.guild}" dió una idea: {ideaMessage}')


def setup(bot):
    bot.add_cog(b_Ideas(bot))
