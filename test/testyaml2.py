import os
import yaml

configFile = open("E:\Dyson\config\\668058103023140872.yml", 'r')
configData = yaml.safe_load(configFile)

 # Asignación de variables friendlys xd
customList = configData["comandos"].keys()

for x in customList:
    print(x)


print(customList)