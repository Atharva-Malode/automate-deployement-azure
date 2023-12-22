from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"Hello": "World"})

@app.route("/bored")
def bored():
    response = requests.get("https://www.boredapi.com/api/activity")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run()