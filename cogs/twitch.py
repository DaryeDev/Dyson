import discord
from discord.ext import commands
import requests
import asyncio
import yaml
import random
from cogs.config import config, getPrefix

authCode = "bearerCode"
clientID = "clientID"


class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.checkUsers(bot))
        self.bot.loop.create_task(self.dataChannels(bot))

    async def dataChannels(self, bot):
        global tokenWorks, token
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            for guild in bot.guilds:
                guild_id = guild.id
                try:
                    configData = config.load(guild_id)
                    demo = 0
                except:
                    demo = 1
                if not demo:
                    try:
                        mainChannel = configData["twitch"]["mainChannel"]
                        channelID = configData["twitch"]["dataChannels"]["followers"]
                        enabled = True
                        payload = {}
                        headers = {
                            'client-id': clientID,
                            'Authorization': authCode
                        }
                        url = f"https://api.twitch.tv/helix/users?login={mainChannel}"
                        response = requests.request("GET", url, headers=headers, data=payload)
                        response = response.json()
                        userID = response['data'][0]['id']
                        url = f"https://api.twitch.tv/helix/users/follows?to_id={userID}"
                        response = requests.request("GET", url, headers=headers, data=payload)
                        response = response.json()
                        followerNo = response['total']

                        followersChannel = bot.get_channel(channelID)
                        await followersChannel.edit(name=f"Seguidores: {followerNo}")

                    except:
                        try:
                            mainChannel = configData["twitch"]["mainChannel"]
                            followersChannel = discord.utils.get(guild.voice_channels, name='%seguidores%',
                                                                 bitrate=64000)
                            print(followersChannel.id)
                            channelID = str(followersChannel.id)
                            data = "{'followers': sipi}"
                            data = data.replace("sipi", channelID)
                            configData["twitch"]["dataChannels"] = yaml.safe_load(data)
                            with open(config.path(guild_id), "w") as f:
                                yaml.dump(configData, f)
                            enabled = True
                            payload = {}
                            headers = {
                                'client-id': clientID,
                                'Authorization': authCode
                            }
                            url = f"https://api.twitch.tv/helix/users?login={mainChannel}"
                            response = requests.request("GET", url, headers=headers, data=payload)
                            response = response.json()
                            userID = response['data'][0]['id']

                            url = f"https://api.twitch.tv/helix/users/follows?to_id={userID}"
                            response = requests.request("GET", url, headers=headers, data=payload)
                            response = response.json()
                            followerNo = response['total']
                            await followersChannel.edit(name=f"Seguidores: {followerNo}")
                        except:
                            pass  # no existe el canal y no se usa la función
                else:
                    print(f"El servidor {guild} está en modo demo")
            await asyncio.sleep(20)

    async def checkUsers(self, bot):
        global tokenWorks, token
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            for guild in bot.guilds:
                guild_id = guild.id
                try:
                    configData = config.load(guild_id)
                    demo = 0
                except:
                    demo = 1
                if not demo:
                    for twitchChannel in configData["twitch"]["channels"]:
                        url = f"https://api.twitch.tv/helix/streams?user_login={twitchChannel}"
                        payload = {}
                        headers = {
                            'client-id': clientID,
                            'Authorization': authCode
                        }
                        response = requests.request("GET", url, headers=headers, data=payload)
                        response = response.json()
                        try:
                            if response['data'][0]['type'] == "live":

                                if configData["twitch"]["channels"][twitchChannel]["isLive"] == 0:
                                    configData["twitch"]["channels"][twitchChannel]["isLive"] = 1
                                    with open(config.path(guild_id), "w") as f:
                                        yaml.dump(configData, f)

                                    message = configData["twitch"]["message"]
                                    canalTwitch = configData["canales"]["canalTwitch"]

                                    user = response['data'][0]['user_name']
                                    message = message.replace("{user}", user)

                                    gameID = response['data'][0]['game_id']
                                    gameURL = f"https://api.twitch.tv/helix/games?id={gameID}"
                                    game = requests.request("GET", gameURL, headers=headers, data=payload)
                                    game = game.json()['data'][0]['name']
                                    message = message.replace("{game}", game)

                                    title = response['data'][0]['title']
                                    message = message.replace("{title}", title)

                                    URL = f"https://twitch.tv/{user}"
                                    message = message.replace("{url}", URL)

                                    userURL = f"https://api.twitch.tv/helix/users?login={user}"
                                    userImg = requests.request("GET", userURL, headers=headers, data=payload)
                                    userImg = userImg.json()['data'][0]['profile_image_url']

                                    embed = discord.Embed(title=title,
                                                          url=f"https://twitch.tv/{user}")

                                    embed.set_image(
                                        url=f"https://static-cdn.jtvnw.net/previews-ttv/live_user_{user.lower()}-1920x1080.jpg?{random.randint(0, 9999999)}")
                                    embed.set_author(name=user, url=URL,
                                                     icon_url=userImg)
                                    embed.set_footer(text="Dyson", icon_url="https://i.imgur.com/JfwkjFL.png")

                                    await self.bot.get_channel(int(canalTwitch)).send(content=message, embed=embed)

                        except:
                            configData["twitch"]["channels"][twitchChannel]["isLive"] = 0
                            config.save(guild_id, configData)

                    await asyncio.sleep(10)

                else:
                    print(f"El servidor {guild} está en modo demo")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mainStreamer(self, ctx, streamer):
        guild_id = ctx.guild.id
        try:
            configData = config.load(guild_id)
        except:
            config.create(guild_id)
            configData = config.load(guild_id)
        try:
            configData["twitch"]["mainChannel"] = streamer.lower()
        except:
            configData["twitch"] = {}
            configData["twitch"]["mainChannel"] = streamer.lower()

        config.save(guild_id, configData)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addstream(self, ctx, streamer):
        guild_id = ctx.guild.id
        try:
            configData = config.load(guild_id)
        except:
            config.create(guild_id)
            configData = config.load(guild_id)
        try:
            configData["twitch"]["channels"][streamer.lower()] = {"isLive": 0}
        except:
            configData["twitch"] = {}
            configData["twitch"]["channels"] = {}
            configData["twitch"]["channels"][streamer.lower()] = {"isLive": 0}

        config.save(guild_id, configData)
        await ctx.send(f'¡{streamer} añadido a la lista de notificaciones de directo!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delstream(self, ctx, streamer):
        guild_id = ctx.guild.id
        try:
            configData = config.load(guild_id)
            try:
                del configData["twitch"]["channels"][streamer.lower()]

                config.save(guild_id, configData)

                await ctx.send(f'¡{streamer} quitado de la lista de notificaciones de directo!')
            except:
                await ctx.send(f'{streamer} no encontrado la lista de notificaciones de directo, ¿lo has escrito bien?')

        except:
            await ctx.send(
                f'{ctx.guild} no tiene ningún streamer configurado, ¡añade alguno con "{getPrefix(guild_id)}addstream" o en el panel de control de Dyson!')


def setup(bot):
    bot.add_cog(twitch(bot))
