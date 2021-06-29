from pyngrok import ngrok

public_url = ngrok.connect(5000, "http")
tunnels = ngrok.get_tunnels()
print(tunnels)

import subprocess

process = subprocess.Popen(["python3.8", "./test/handler.py"], stdout=subprocess.PIPE)
output = process.communicate()[0]

# while True:
#     a=1
