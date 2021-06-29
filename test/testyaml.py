import yaml
fname = "dota.yaml"

configFile = open("E:\Dyson\config\example.yml", 'r')
configData = yaml.safe_load(configFile)
with open(fname, "w") as f:
    yaml.dump(configData, f)

with open(fname) as f:
    newdct = yaml.safe_load(f)

print (newdct)
newdct["ideas"] = {"ideasNo": 0, "ideas": {"ideaNo": {}}}

with open(fname, "w") as f:
    yaml.dump(newdct, f)