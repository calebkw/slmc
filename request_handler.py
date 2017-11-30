import 
from flask import Flask, request, jsonify
app= Flask(__name__)


@app.route("http://vcm-1612.vm.duke.edu:5000/api/classify", methods=['POST'])
def classify():
    image = { "img": img}
    UUID = {"UUID": UUID}
    arr = [image, UUID]
    return jsonify(arr)

@app.route("http://vcm-1612.vm.duke.edu:5000/api/num_requests", methods=['GET'])
def output():



if __name__ == "__main__"
    app.run(host='0.0.0.0', port=80)

