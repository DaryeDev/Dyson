import requests

S = requests.Session()

URL = "https://es.wikihow.com/api.php"

SEARCHPAGE = "novia"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": SEARCHPAGE
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)

try:
    print(DATA['query']['search'][0]['pageid'])
    print(f"Cómo {DATA['query']['search'][0]['title']}")
    print(f"https://es.wikihow.com/?curid={DATA['query']['search'][0]['pageid']}")
except:
    print("No hay xd")
    pass
