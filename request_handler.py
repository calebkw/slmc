import 
from flask import Flask, request, jsonify
app= Flask(__name__)


@app.route("/data", methods=['POST'])
def classify():
    image = { "img": img}
    UUID = {"UUID": UUID}
    arr = [image, UUID]
    return jsonify(arr)
