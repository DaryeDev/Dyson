import requests
wikihow = 0
S = requests.Session()

URL = "https://es.wikihow.com/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "1",
    "prop": "info|extracts",
    "inprop": "url"
}
while wikihow == 0:
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    RANDOMS = DATA["query"]["random"]

    for r in RANDOMS:
        print(r)
        if not str(r["title"]).startswith(("Usuario", "User", "Imagen", "Plantilla")):
            wikihow = 1
            print(f'https://es.wikihow.com/?curid={r["id"]}')