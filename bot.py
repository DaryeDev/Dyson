import discord
from cogs.config import config
import yaml
from discord.ext import commands


# noinspection PyBroadException
def getPrefix(bot, message):
    if type(message) == str or int:
        guildID = message
    else:
        guildID = str(message.guild.id)
    try:
        prefixes = config.load("prefixes")
        return prefixes[guildID]
    except:
        return "d."

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=getPrefix, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    with open("cogs.yaml", "r") as f:
        cogList = yaml.safe_load(f)
    for cog in cogList["cogs"]:
        if cogList["cogs"][cog]["enabled"]:
            bot.load_extension(f"cogs.{cog}")
            print(cog)
    print("¡Todos los módulos cargados!")

    print(f"¡Listo! ¡{bot.user} está online!")

    activity = discord.Activity(name='yeet', type=discord.ActivityType.streaming)
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    print(message.author, "dijo '", message.content, "' en el canal", message.channel, "(ID:", message.channel.id, ")")
    await bot.process_commands(message)


@bot.command(name="load", hidden=True)
async def load(ctx, modulo):
    if ctx.author.id == 439470338150236162:
        try:
            bot.load_extension(f"cogs.{modulo}")
            await ctx.send(f"Módulo {modulo} cargado correctamente!")
            print(f"Módulo {modulo} cargado correctamente!")
        except discord.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f"Hubo un error cargando el modulo {modulo}")
            print(f"Hubo un error cargando el modulo {modulo}")
    else:
        pass


@bot.command(name="unload", hidden=True)
async def unload(ctx, modulo):
    if ctx.author.id == 439470338150236162:
        try:
            bot.unload_extension(f"cogs.{modulo}")
            await ctx.send(f"Módulo {modulo} descargado correctamente!")
            print(f"Módulo {modulo} descargado correctamente!")
        except discord.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f"Hubo un error descargando el modulo {modulo}")
            print(f"Hubo un error descargando el modulo {modulo}")
    else:
        pass


@bot.command(name="reload", hidden=True)
async def reload(ctx, modulo):
    if ctx.author.id == 439470338150236162:
        try:
            bot.reload_extension(f"cogs.{modulo}")
            await ctx.send(f"Módulo {modulo} recargado correctamente!")
            print(f"Módulo {modulo} recargado correctamente!")
        except discord.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f"Hubo un error recargando el modulo {modulo}")
            print(f"Hubo un error recargando el modulo {modulo}")
    else:
        pass


@bot.command(name="cogadd", hidden=True, aliases=["cogenable"])
async def cogadd(ctx, modulo):
    with open("cogs.yaml", "r") as f:
        cogList = yaml.safe_load(f)
    if ctx.author.id == 439470338150236162:
        cogList["cogs"][modulo] = {"enabled": True}
        with open("cogs.yaml", "w") as f:
            yaml.dump(cogList, f)
        await ctx.send(f"Módulo {modulo} añadido correctamente!")
        print(f"Módulo {modulo} añadido correctamente!")
        try:
            bot.load_extension(f"cogs.{modulo}")
        except discord.ext.commands.errors.ExtensionNotFound:
            print(f"{modulo} ya estaba cargado.")
    else:
        pass

@bot.command(name="cogdel", hidden=True, aliases=["cogdisable"])
async def cogdel(ctx, modulo):
    with open("cogs.yaml", "r") as f:
        cogList = yaml.safe_load(f)
    if ctx.author.id == 439470338150236162:
        cogList["cogs"][modulo] = {"enabled": False}
        with open("cogs.yaml", "w") as f:
            yaml.dump(cogList, f)
    else:
        pass


token = ""
bot.run(token)
