from discord.ext import commands
from cogs.config import config


class sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx, cuentaTwitch):
        if not ctx.author.bot:
            users = config.load("twitch")
            author_id = str(ctx.author.id)
            users[author_id] = cuentaTwitch
            config.save("twitch", users)
            await ctx.send(f"¡{ctx.author.mention} ha sido vinculado con la cuenta de Twitch '{cuentaTwitch}'!")


def setup(bot):
    bot.add_cog(sync(bot))
