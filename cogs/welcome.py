from discord.ext import commands
import json
import discord
from discord.ext.commands import Cog
from cogs.config import config
import yaml


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        print("Se ha metido alguien")
        guild_id = member.guild.id
        configData = config.load(guild_id)

        # Asignación de variables friendlys xd
        welcomeMD = configData["wcgb"]["welcome"]['welcomeMD']
        print(welcomeMD)
        welcomeMessage = configData["wcgb"]["welcome"]['welcomeMessage']
        print(welcomeMessage)
        usuario = member.mention
        welcomeMessage = welcomeMessage.replace("{usuario}", usuario)
        welcomeMD = welcomeMD.replace("{usuario}", usuario)
        print(welcomeMD)
        print(welcomeMessage)

        nombreServidor = f"""**{member.guild}**"""
        welcomeMessage = welcomeMessage.replace("{nombreServidor}", nombreServidor)
        welcomeMD = welcomeMD.replace("{nombreServidor}", nombreServidor)

        numeroMiembros = len([m for m in member.guild.members if not m.bot])
        welcomeMessage = welcomeMessage.replace("{numeroMiembros}", str(numeroMiembros))
        welcomeMD = welcomeMD.replace("{numeroMiembros}", str(numeroMiembros))

        canalRoles = f"""<#{configData["canales"]['canalRoles']}>"""
        welcomeMessage = welcomeMessage.replace("{canalRoles}", canalRoles)
        welcomeMD = welcomeMD.replace("{canalRoles}", canalRoles)

        canalReglas = f"""<#{configData["canales"]['canalReglas']}>"""
        welcomeMessage = welcomeMessage.replace("{canalReglas}", canalReglas)
        welcomeMD = welcomeMD.replace("{canalReglas}", canalReglas)

        canalIdeas = f"""<#{configData["canales"]['canalIdeas']}>"""
        welcomeMessage = welcomeMessage.replace("{canalIdeas}", canalIdeas)
        welcomeMD = welcomeMD.replace("{canalIdeas}", canalIdeas)

        welcomeRole = configData["wcgb"]["welcome"]['welcomeRole']
        wcgbEnable = configData["wcgb"]['wcgbEnable']
        welcomeChannelID = configData["wcgb"]["welcome"]['welcomeChannelID']

        print(welcomeRole)
        print(welcomeChannelID)
        print(welcomeMD)
        print(welcomeMessage)
        print(wcgbEnable)

        if wcgbEnable:  # Mira si los mensajes de bienvenida y despedida están activados
            await self.bot.get_channel(int(welcomeChannelID)).send(welcomeMessage)
            await member.send(welcomeMD)
            role = discord.utils.get(member.guild.roles, name=welcomeRole)
            await member.add_roles(role)

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 668132895197757442:
            guild_id = payload.guild_id
            if guild_id == 668058103023140872:
                if payload.emoji.name == "✅":
                    guild = self.bot.get_guild(payload.guild_id)
                    user = guild.get_member(payload.user_id)
                    before = discord.utils.get(guild.roles, name="Revirgo")
                    after = discord.utils.get(guild.roles, name="Virgo")
                    await user.remove_roles(before)
                    await user.add_roles(after)

    @Cog.listener()
    async def on_member_remove(self, member):
        print("Se ha pirado alguien")
        guild_id = member.guild.id
        configData = config.load(guild_id)

        # Asignación de variables friendlys xd
        goodbyeMessage = configData["wcgb"]['goodbye']['goodbyeMessage']

        usuario = member.name
        print(usuario)
        goodbyeMessage = goodbyeMessage.replace("{usuario}", f"""*{usuario}*""")

        nombreServidor = f"""**{member.guild}**"""
        goodbyeMessage = goodbyeMessage.replace("{nombreServidor}", nombreServidor)

        numeroMiembros = len([m for m in member.guild.members if not m.bot])
        goodbyeMessage = goodbyeMessage.replace("{numeroMiembros}", str(numeroMiembros))

        canalRoles = f"""<#{configData["canales"]['canalRoles']}>"""
        goodbyeMessage = goodbyeMessage.replace("{canalRoles}", canalRoles)

        canalReglas = f"""<#{configData["canales"]['canalReglas']}>"""
        goodbyeMessage = goodbyeMessage.replace("{canalReglas}", canalReglas)

        canalIdeas = f"""<#{configData["canales"]['canalIdeas']}>"""
        goodbyeMessage = goodbyeMessage.replace("{canalIdeas}", canalIdeas)
        wcgbEnable = configData["wcgb"]['wcgbEnable']
        goodbyeChannelID = configData["wcgb"]['goodbye']['goodbyeChannelID']

        print(goodbyeChannelID)
        print(goodbyeMessage)
        print(wcgbEnable)

        if wcgbEnable:  # Mira si los mensajes de bienvenida y despedida están activados
            await self.bot.get_channel(int(goodbyeChannelID)).send(goodbyeMessage)


def setup(bot):
    bot.add_cog(Welcome(bot))
