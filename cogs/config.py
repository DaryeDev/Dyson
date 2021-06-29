# Emojis de conf:
# <:Dyson:752915533237846137>
# <:DysonTag:752919155849691276>
# <:DysonWelcome:752881754003603461>
# <:DysonUserTag:752881754184089661>
# <:DysonTwitch:752881754150535228>
# <:DysonReglas:752881753848414219>
# <:DysonMessage2:752881754217381888>
# <:DysonMessage1:752881753840156683>
# <:DysonIdea:752881754313851010>
# <:DysonGoodbye:752881754074906675>
# <:DysonConfig:752881753928237108>
# <:DysonChannels:752881753911459971>
# <:QuienJuega:752881754259456040>
# <:DysonExit:752920165854871632>
# <:DysonOn:752932314912129054>
# <:DysonOff:752932314744356944>
import os
import yaml
import json


def getPrefix(message):
    if type(message) == str or int:
        guildID = message
    else:
        guildID = str(message.guild.id)
    try:
        with open('config/prefixes.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes[guildID]
    except:
        return "d."


class config:

    @staticmethod
    def create(guildID):  # config.create(guild_id)
        with open('config/prefixes.json', 'r') as f:
            prefixes = json.load(f)
            prefixes[str(guildID)] = 'd.'
            with open('config/prefixes.json', 'w+') as f:
                json.dump(prefixes, f, indent=4)

            configFile = open("config/example.yml", 'r')
            configTemplate = yaml.safe_load(configFile)
            with open(f"config/{str(guildID)}.yml", "w+") as f:
                yaml.dump(configTemplate, f)

    @staticmethod
    def load(guildID):  # configData = config.load(guild_id)
        base_dir = 'config'
        configName = str(guildID) + '.yml'
        configPath = str(os.path.join(base_dir, configName))
        configFile = open(configPath, 'r')
        configData = yaml.safe_load(configFile)
        return configData

    @staticmethod
    def path(guildID):  # configPath = config.path(guild_id)
        base_dir = 'config'
        configName = str(guildID) + '.yml'
        configPath = str(os.path.join(base_dir, configName))
        return configPath

    @staticmethod
    def save(guildID, configData):  # Su uso normal sería "config.save(guild_id, configData)"
        base_dir = 'config'
        configName = str(guildID) + '.yml'
        configPath = str(os.path.join(base_dir, configName))
        with open(configPath, "w") as f:
            yaml.dump(configData, f)

# class config(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         process = subprocess.Popen(["python3.8", "./cogs/configTools/startNgrok.py"], stdout=subprocess.PIPE)
#         output = process.communicate()[0]
#         public_url = ngrok.connect(5000, "http")
#         tunnels = ngrok.get_tunnels()
#         url = str(tunnels[1]).replace('NgrokTunnel: "', "")
#         url = url.replace('" -> "http://localhost:5000"', "")
#         print(url)
