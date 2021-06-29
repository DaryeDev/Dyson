import yaml
fname = "dota.yaml"
o = "o"
with open("example.yml", "r") as f:
    configData = yaml.safe_load(f)
print(configData["twitch"])
data = "{'date': %fecha%, 'notified': 0}"
data = data.replace("%fecha%", "23/03")
configData["calendar"]["birthdays"]["439470338150236162"] = yaml.safe_load(data)
print(configData["twitch"])
with open("example.yml", "w") as f:
    yaml.dump(configData, f)
# configData["twitch"]["aaa"][o]["isLaive"] = 1
try:
    o=o.lower()
    if configData["twitch"]["channels"][o]["isLive"] == 0:
        configData["twitch"]["channels"][o]["isLive"] = 1
        with open("example.yml", "w") as f:
            yaml.dump(configData, f)
    else:
        print("si")
except:
    print("puta")