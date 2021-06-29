from discord.ext import commands
from discord.ext.commands import Cog
from cogs.config import config, getPrefix


class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        try:
            guild_id = message.guild.id
            prefix = getPrefix(guild_id)
            configData = config.load(guild_id)

            for x in configData["customCommands"]:
                if message.content.lower().startswith(prefix + x):
                    await message.channel.send(configData["customCommands"][x]['command'])
        except:
            pass

    @commands.command(name="add", brief='Añade nuevos comandos personalizados para tu server.')
    @commands.has_permissions(administrator=True)
    async def add(self, ctx, comando, respuesta):
        guild_id = ctx.guild.id
        prefix = getPrefix()
        try:
            configData = config.load(guild_id)
        except:
            config.create(guild_id)
            configData = config.load(guild_id)

        if not comando in configData["customCommands"]:
            configData["customCommands"][comando] = {'command': respuesta}

            config.save(guild_id, configData)

            await ctx.send(f'¡Comando "{prefix}{comando}" creado con éxito!')

        else:
            await ctx.send("Ese comando ya existe, intenta con otro.")

    @commands.command(name="edit", brief='Edita los comandos personalizados de tu server.')
    @commands.has_permissions(administrator=True)
    async def edit(self, ctx, comando, respuesta):
        guild_id = ctx.guild.id
        prefix = getPrefix()
        try:
            configData = config.load(guild_id)
        except:
            config.create(guild_id)
            configData = config.load(guild_id)

        if comando in configData["customCommands"]:
            configData["customCommands"][comando]["command"] = respuesta

            config.save(guild_id, configData)

            await ctx.send(f'¡Comando "{prefix}{comando}" editado con éxito!')

        else:
            await ctx.send("Ese comando no existe, intenta con otro.")

    @commands.command(name="delete", brief='Elimina un comando personalizado de tu server.')
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx, comando):
        guild_id = ctx.guild.id
        try:
            configData = config.load(guild_id)
        except:
            config.create(guild_id)
            configData = config.load(guild_id)

        if comando in configData["customCommands"]:
            del configData['customCommands'][comando]
            config.save(guild_id, configData)
            await ctx.send(f'¡Comando "{getPrefix()}{comando}" borrado con éxito!')
        else:
            await ctx.send("Ese comando no existe, intenta con otro.")


def setup(bot):
    bot.add_cog(CustomCommands(bot))
