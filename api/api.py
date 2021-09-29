"""
This backend will be namespaced like the following:
 - /api/{something} : This will be served by flask, as an API
 - / : This will be the React application, which will have it's own routes

"""
import time
from flask import Flask, request
from web3 import Web3

app = Flask(__name__, static_folder="../build", static_url_path="/")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/code")
def get_contract_code():
    args = request.args
    address = args["address"]
    print(address)
    print(Web3.isAddress(address))
    return {"time": time.time()}
