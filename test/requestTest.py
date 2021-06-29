import flask
from pyngrok import ngrok
from flask import request, jsonify
import os
import yaml
# import subprocess
#
# process = subprocess.Popen(["./ngrok/ngrok", "http", "localhost:5000"], stdout=subprocess.PIPE)
# output = process.communicate()[0]


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hey! No deberías estar aquí xddd</h1>
<p>No te metas donde no te llaman xd</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/a', methods=['GET'])
def api_a():
    with open("/home/ubuntu/Dyson/example.yml", "r") as f:
        users = yaml.safe_load(f)
    users["sech"] = "a"
    with open("/home/ubuntu/Dyson/examplo.yml", "w") as f:
        yaml.dump(users, f)
    return "a"

@app.route('/test', methods=['GET'])
def api_test():
    print("Test")
    return "Test"

app.run(host="0.0.0.0")