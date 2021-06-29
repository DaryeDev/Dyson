import asyncio
import discord
from discord.ext import commands


class Sonidos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='bruh',
        description='Esto es un gran Bruh Moment. Reproduce el sonido de "bruh" en el canal de voz en el que estés.',
        brief='Reproduce el sonido de "bruh" en el canal de voz en el que estés.'
    )
    async def bruh(self, ctx):
        """Esto es un gran Bruh Moment. Reproduce el sonido de "bruh" en el canal de voz en el que estés."""
        user = ctx.author
        connected = ctx.author.voice
        if connected:
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio('sounds/bruh.ogg'), after=lambda e: print('Bruh Momento'))
            await asyncio.sleep(1)
            await vc.disconnect()
        else:
            await ctx.channel.send('No estás en un canal de voz, bruh xd')

    @commands.command(
        name='phub',
        description='Ambos sabemos lo que significa 7u7.',
        brief='Ambos sabemos lo que significa 7u7.'
    )
    async def phub(self, ctx):
        """Ambos sabemos lo que significa 7u7."""
        user = ctx.author
        connected = ctx.author.voice
        if connected:
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio('sounds/ph.mp3'), after=lambda e: print('Phub'))
            await asyncio.sleep(5)
            await vc.disconnect()
        else:
            await ctx.channel.send('No estás en un canal de voz, bruh xd')

    @commands.command(
        name='comunismo',
        description='Restauremos la Unión Soviética!',
        brief='Restauremos la Unión Soviética!'
    )
    async def comunismo(self, ctx):
        """Restauremos la Unión Soviética!"""
        user = ctx.author
        connected = ctx.author.voice
        if connected:
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio('sounds/communism.ogg'), after=lambda e: print('comunos'))
            await asyncio.sleep(5)
            await vc.disconnect()
        else:
            await ctx.channel.send('No estás en un canal de voz, bruh xd')

    @commands.command(
        name='oof',
        description='oof',
        brief='oof'
    )
    async def oof(self, ctx):
        """oof"""
        user = ctx.author
        connected = ctx.author.voice
        if connected:
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio('sounds/oof.ogg'), after=lambda e: print('oof'))
            await asyncio.sleep(5)
            await vc.disconnect()
        else:
            await ctx.channel.send('No estás en un canal de voz, bruh xddd')


def setup(bot):
    bot.add_cog(Sonidos(bot))
