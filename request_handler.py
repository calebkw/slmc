import sys
sys.path.insert(0,'/')
from flask import Flask, request, jsonify
import io
from PIL import Image as im
import base64
import get_prediction
import numpy as np
app= Flask(__name__)

calls = 0

@app.route("/requests", methods=['GET'])
def request_total():
    """

    :return: the total number of requests made to the service
    most recent reboot as JSON
    """

    global calls
    calls += 1
    output = {"requests": calls}
    return jsonify(output)

@app.route("/image/classify", methods=['POST'])
def request_classify():
    """
    Takes in the image as a JSON and coverts to nd array

    :return: the label of the image and the results 
    """

    global calls
    calls += 1
    label = []
    try:
        input = request.json['images']
    except:
        output = "Input data is not formatted correctly."
        return jsonify(output), 400
    try:
        output = {'classified':[]}
        for image in input:
            im_data = base64.b64decode(image['data'])
            im_data = np.array(im.open(io.BytesIO(im_data)))
            prediction = get_prediction(im_data)
            current_im_dict = {'name': image['name'], 'prediction': prediction}
            output['classified'].append(current_im_dict)

    except:
        output = "Internal Error"
        return jsonify(output), 500


@app.route("/testing", methods=['POST'])
def test_return():
    global calls
    calls += 1

    input = request.json

    return jsonify(input)

