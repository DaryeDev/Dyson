import json
import pprint
import urllib
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import discord
import requests
from discord.ext import commands
from discord.ext.commands import bot


class Acciones(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def respuestaMensaje(accion):
        global url
        apikey = "Z20FPG65VAWS"
        lmt = 1
        r = requests.get(
            "https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (accion, apikey, lmt))

        if r.status_code == 200:
            pp = pprint.PrettyPrinter(indent=4)
            gif = json.loads(r.content)
            for i in range(len(gif['results'])):
                url = gif['results'][i]['media'][0]['gif']['url']

    @commands.command(name='hug',
                      brief='Abraza a tu compañero uwu')
    async def hug(self, ctx, user):
        """Abraza a tu compañero uwu."""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        Acciones.respuestaMensaje("hug")
        embed.set_image(url=url)
        try:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** abrazó a **{user}**. uwu""")
        except discord.ext.commands.errors.MissingRequiredArgument:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** se abrazó a sí mismo, esto es un poco triste...""")

        await ctx.send(embed=embed)

    @commands.command(name='hostia',
                      brief='Dale una hostia a alguien xd')
    async def hostia(self, ctx, user):
        """Dale una hostia a alguien xd"""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        Acciones.respuestaMensaje("slap")
        embed.set_image(url=url)
        try:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** le dió una hostia a **{user}**. 😈""")
        except discord.ext.commands.errors.MissingRequiredArgument:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** se dió una hostia a sí mismo... ¿Estás bien?""")

        await ctx.send(embed=embed)

    @commands.command(name='kill',
                      brief='Literalmente mata a alguien xddd')
    async def kill(self, ctx, user):
        """Literalmente mata a alguien xddd"""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        print(user)
        print(ctx.author.id)
        try:
            if user != ("<@741962880097845340>" and "<@!741962880097845340>") :
                embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** puto mató a **{user}**. 😎✨""")
                Acciones.respuestaMensaje("kill you")
                embed.set_image(url=url)
                await ctx.send(embed=embed)
            else:
                async with ctx.channel.typing():
                    bg = Image.open('cogs/img/CallAnAmbulance....png').convert("RGBA")
                    width, height = bg.size
                    userIcon = ctx.author.avatar_url
                    img_data = requests.get(userIcon).content
                    with open('cogs/img/userIcon.png', 'wb') as handler:
                        handler.write(img_data)
                    userIcon = Image.open('cogs/img/userIcon.png').convert("RGBA")
                    mask = Image.open("cogs/img/circuloMask.png").convert("L")
                    userIcon = userIcon.resize((100, 100), Image.ANTIALIAS)
                    userIcon = ImageOps.fit(userIcon, mask.size, centering=(0.5, 0.5))
                    userIcon.putalpha(mask)
                    userIcon = userIcon.resize((100, 100), Image.ANTIALIAS)

                    text_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                    text_img.paste(bg, (0, 0))
                    text_img.paste(userIcon, (90, -5), mask=userIcon)
                    text_img.save("cogs/img/killDyson.png", format="png")
                    file = discord.File("cogs/img/killDyson.png", filename="image.png")
                    embed.set_image(url="attachment://image.png")
                    embed.add_field(name="‎", value="...")
                    await ctx.send(file=file, embed=embed)


        except discord.ext.commands.errors.MissingRequiredArgument:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** se puto mató. 😎✨""")
            Acciones.respuestaMensaje("kms")
            embed.set_image(url=url)
            await ctx.send(embed=embed)


    @commands.command(name='kiko',
                      brief='Te puto matas. Momento xd.')
    async def kiko(self, ctx):
        """Te puto matas. Momento xd."""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** se puto mató. 😎✨""")
        Acciones.respuestaMensaje("kms")
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(name='cry',
                      brief='WAAAH WAAAH',
                      alias="llorar")
    async def cry(self, ctx):
        """WAAAH WAAAH"""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** se puso a llorar. 😭""")
        Acciones.respuestaMensaje("cry")
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(name='cat',
                      brief='Miau xd',
                      alias="gato")
    async def cat(self, ctx):
        """WAAAH WAAAH"""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** ahora tiene un gatito. 😼""")
        Acciones.respuestaMensaje("cat")
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(name='heal',
                      brief='Curas a quien quieras.')
    async def heal(self, ctx, user):
        """Curas a quien quieras"""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))

        try:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** curó a **{user}** 💉""")
            Acciones.respuestaMensaje("heal")
        except discord.ext.commands.errors.MissingRequiredArgument:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** se curó 💉""")
            Acciones.respuestaMensaje("heal")

        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(name='horny',
                      brief='Mandas a la horny jail a alguien horny.')
    async def horny(self, ctx, user):
        """Mandas a la horny jail a alguien horny."""
        embed = discord.Embed(colour=discord.Colour(0x9013fe))

        try:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** mandó a **{user}** a la Horny Jail""")
        except discord.ext.commands.errors.MissingRequiredArgument:
            embed.add_field(name="‎", value=f"""**<@!{ctx.author.id}>** está horny. Tened cuidado :0""")

        embed.set_image(url="https://media1.tenor.com/images/062ed2c1ab2756d774367ef0f8a1f53b/tenor.gif?itemid=17582752")
        await ctx.send(embed=embed)

    @commands.command(name='bonk',
                      brief='bonk.')
    async def bonk(self, ctx, user):
        """bonk."""
        actionUser = ctx.message.content.replace("d.bonk ", "")
        embed = discord.Embed(colour=discord.Colour(0x9013fe))
        embed.add_field(name="‎", value=f"""Bonk a  **{actionUser}** de parte de **<@!{ctx.author.id}>**""")
        embed.set_image(
            url="https://media1.tenor.com/images/ae34b2d6cbac150bfddf05133a0d8337/tenor.gif?itemid=14889944")
        await ctx.send(embed=embed)
        #bonk.

def setup(bot):
    bot.add_cog(Acciones(bot))