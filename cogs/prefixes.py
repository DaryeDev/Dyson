from cogs.config import config
from discord.ext import commands


class prefixes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="prefix", brief='Cambia el prefijo de Dyson en tu server.', aliases=['prefijo', 'px'])
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefijo):
        prefixConfig = config.load("prefixes")
        prefixConfig[str(ctx.guild.id)] = prefijo
        config.save("prefixes", prefixConfig)
        await ctx.send(f"Prefijo cambiado a {prefijo}")


def setup(bot):
    bot.add_cog(prefixes(bot))
