import typing
from discord.ext import commands


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx, minutes: typing.Optional[int] = 5):
        time = minutes*60
        link = await ctx.channel.create_invite(max_age=time)
        if minutes != 0:
            await ctx.send(f"Aquí tienes una invitación de {minutes} minutos a **{ctx.guild}**: {link}")
        else:
            await ctx.send(f"Aquí tienes una invitación a **{ctx.guild}**: {link}")


def setup(bot):
    bot.add_cog(Invite(bot))
