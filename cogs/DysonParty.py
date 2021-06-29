from discord.ext import commands
import discord
from discord.ext.commands import bot
from discord.utils import get
import cogs.config as config
import string
import random

client = discord.Client()


class DysonParty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="party",
                      brief='Da ideas a Darye para mejorar a Dyson.', aliases=["play", "jugar"])
    async def party(self, ctx, juego=None, numPersonas=None):
        if None != juego:
            for guild in bot.guilds:
                guild_id = guild.id
                configData = config.load(guild_id)
                try:
                    if configData["DysonParty"]["enabled"]:
                        if configData["DysonParty"]["mode"] == "public":
                            DysonPartyGuild = bot.get_guild(
                                "752152989757866025")  # find ID by right clicking on server icon and choosing "copy id" at the bottom
                            if guild.get_member(ctx.author.id) is not None:
                                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
                                role = await ctx.guild.create_role(name=code)
                                await ctx.message.author.add_roles(role)
                                admin_role = get(guild.roles, name=code)
                                overwrites = {
                                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                                    guild.me: discord.PermissionOverwrite(read_messages=True),
                                    admin_role: discord.PermissionOverwrite(read_messages=True)
                                }
                                salaTexto = await guild.create_text_channel(f'sala-{code}', overwrites=overwrites,
                                                                            channel="Tu Sala")
                                salaVoz = await guild.create_voice_channel(f'Sala {code}', overwrites=overwrites,
                                                                           channel="Tu Sala", user_limit=numPersonas)

                                await ctx.send(
                                    f"Sala creada, el código es {code}, el juego es '{juego}' y el máximo de personas es {numPersonas}")

                                DysonPartyChannel = configData["DysonParty"]["channel"]
                                await self.bot.get_channel(DysonPartyChannel).send(
                                    f'{ctx.author}, del servidor "{ctx.guild}", quiere jugar a {juego}. Jugad juntos en https://discord.gg/Ws52Dfw')
                        else:
                            await ctx.send(
                                f"Para usar esta función tienes que estar en el servidor de DysonParty, puedes unirte aquí: https://discord.gg/Ws52Dfw")
                    else:
                        await ctx.send(
                            f"DysonParty no está habilitado por los administradores de este servidor. Habla con ellos si quieres que esta función se active (Se activa poniendo 'd.enable DysonParty')")

                except:
                    await ctx.send(
                        f"DysonParty no está habilitado por los administradores de este servidor. Habla con ellos si quieres que esta función se active (Se activa poniendo 'd.enable DysonParty')")
        else:
            await ctx.send("No has elegido ningún juego, vuelve a mandar el comando con el juego al que quieras jugar.")


def setup(bot):
    bot.add_cog(DysonParty(bot))
