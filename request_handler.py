import sys
sys.path.insert(0,'/')
from flask import Flask, request, jsonify
import io
from PIL import Image as im
import base64
from get_prediction import get_prediction
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

@app.route("/classify", methods=['POST'])
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
            # encode from unicode to utf-8, then decode to bytes
            im_data = base64.b64decode((image['data'].encode('utf-8')[2:-1]))
            # read as image data, save in ndarray
            im_data = np.array(im.open(io.BytesIO(im_data)))
            raw_prediction = get_prediction(im_data)
            prediction =[raw_prediction[0],  np.ndarray.tolist(raw_prediction[1])]
            current_im_dict = {'name': image['name'], 'prediction': prediction}
            output['classified'].append(current_im_dict)

    except:
        output = "Internal Error"
        return jsonify(output), 500

    return jsonify(output)

@app.route("/testing", methods=['POST'])
def test_return():
    global calls
    calls += 1

    input = request.json

    return jsonify(input)

