import discord
from discord.ext import commands
from config import server_id, reaction_roles


class roles(commands.Cog):
    # COG init
    def __init__(self, bot):
        self.bot = bot

    async def reaction(self, payload, r_type=None):
        if payload.guild_id == server_id:
            for reaction_info in reaction_roles:
                if payload.message_id == reaction_info[0]:
                    if payload.emoji.name == reaction_info[2]:
                        guild = self.bot.get_guild(payload.guild_id)
                        user = guild.get_member(payload.user_id)
                        role = discord.utils.get(guild.roles, name=reaction_info[1])
                        if r_type == 'remove':
                            await user.remove_roles(role)
                        if r_type == 'add':
                            await user.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await roles.reaction(self, payload=payload, r_type='add')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        await roles.reaction(self, payload=payload, r_type='remove')


def setup(bot):
    bot.add_cog(roles(bot))
