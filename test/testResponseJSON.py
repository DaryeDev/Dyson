import requests
mainChannel = "Darye"
payload = {}
headers = {
                            'client-id': 'a',
                            'Authorization': 'Bearer b'
                        }
url = f"https://api.twitch.tv/helix/users?login={mainChannel}"
response = requests.request("GET", url, headers=headers, data=payload)
response = response.json()
print(response)