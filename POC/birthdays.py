import yaml
from datetime import date

today = date.today()
todayDate = today.strftime("%d/%m")

with open("../example.yml", "r") as f:
    configData = yaml.safe_load(f)
for birthboi in configData["calendar"]["birthdays"]:
    birthdate = configData["calendar"]["birthdays"][birthboi]
    print (birthdate)
    if todayDate == birthdate:
        print(f"Hoy es el cumpleaños de {birthboi}, ¡felicidades!")
    else:
        print(f"Hoy no es el cumpleaños de {birthboi}, cara triste")

print(todayDate)
