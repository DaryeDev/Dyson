import yaml
import os
base_dir = "config"
twitchFile = "twitch.yml"
twitchPath = str(os.path.join(base_dir, twitchFile))
with open(twitchPath, "r") as f:
    users = yaml.safe_load(f)
for twitchUser in users:
    print(users[twitchUser])