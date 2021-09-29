"""
This backend will be namespaced like the following:
 - /api/{something} : This will be served by flask, as an API
 - / : This will be the React application, which will have it's own routes

"""
import os
import json

import time
from flask import Flask, request
from web3 import Web3
import requests


app = Flask(__name__, static_folder="../build", static_url_path="/")

API_KEY = os.getenv("ETHERSCAN_API_KEY")
URL = "https://api.etherscan.io/api"


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/code")
def get_contract_code():
    args = request.args
    address = args["address"]
    print(f"fetching {address}")
    req = requests.get(
        URL,
        {
            "module": "contract",
            "action": "getsourcecode",
            "address": address,
            "apikey": API_KEY,
        },
    )
    ans = req.json()
    res = ans["result"][0]

    try:
        files = json.loads(res["SourceCode"][1:-1])
    except json.JSONDecodeError:
        files = {"single_file": res["SourceCode"]}
    # print(Web3.isAddress(address))
    return files
