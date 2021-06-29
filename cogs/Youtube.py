from cogs.config import config
from discord.ext import commands
import urllib
import json

class YoutubeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='subs')
    async def subs(self, ctx):
        guild_id = ctx.guild.id
        configData = config.load(guild_id)
        channelID = configData['youtube']["channelID"]
        ytKey = configData['youtube']['key']
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+channelID+"&key="+ytKey).read()
        subsYT = json.loads(data)['items'][0]["statistics"]["subscriberCount"]
        await ctx.channel.send(subsYT)

def setup(bot):
    bot.add_cog(YoutubeCog(bot))