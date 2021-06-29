global clientID, authCode
import discord
from discord.ext import commands
import requests
import asyncio
import os
import yaml

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.checkUsers())

    async def checkUsers(self, bot):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            for guild in bot.guilds:

                guild_id = guild.id
                base_dir = 'config'
                configName = str(guild_id) + '.yml'
                print(os.path.join(base_dir, configName))
                configFile = open(os.path.join(base_dir, configName), 'r')
                configData = yaml.safe_load(configFile)

                for twitchChannel in configData["twitch"]["channels"].keys():

                    url = f"https://api.twitch.tv/helix/streams?user_login={twitchChannel}"
                    payload = {}
                    headers = {
                        'client-id': clientID,
                        'Authorization': authCode
                    }
                    response = requests.request("GET", url, headers=headers, data=payload)
                    response = response.json()

                    if configData["twitch"]["channels"][twitchChannel]["isLive"] == 0:
                        if response['data'][0]['type'] == "live":

                            configData["twitch"]["channels"][twitchChannel]["isLive"] = 1
                            with open(os.path.join(base_dir, configName), "w") as f:
                                yaml.dump(configData, f)

                            message = configData["twitch"]["message"]
                            canalTwitch = configData["canales"]["canalTwitch"]

                            user = response['data'][0]['user_name']
                            message = message.replace("{user}", user)

                            gameID = response['data'][0]['game_id']
                            gameURL = f"https://api.twitch.tv/helix/games?id={gameID}"
                            game = requests.request("GET", gameURL, headers=headers, data=payload)
                            game = game.json()['data'][0]['game']
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
                                url=f"https://static-cdn.jtvnw.net/previews-ttv/live_user_{user}-1920x1080.jpg")
                            embed.set_author(name=user, url=URL,
                                             icon_url=userImg)
                            embed.set_footer(text="Dyson", icon_url="https://i.imgur.com/JfwkjFL.png")

                            await self.bot.get_channel(int(canalTwitch)).send(
                                content=message,
                                embed=embed)

                        else:
                            if response['data'][0]['type'] != "live":
                                configData["twitch"]["channels"][twitchChannel]["isLive"] = 0
                                with open(os.path.join(base_dir, configName), "w") as f:
                                    yaml.dump(configData, f)
            await asyncio.sleep(5)

def setup(bot):
    bot.add_cog(twitch(bot))