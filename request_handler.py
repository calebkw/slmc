import sys
from flask import Flask, request, jsonify
import io
import base64
import numpy as np
from PIL import Image as Im
from get_prediction import get_prediction

sys.path.insert(0, '/')
app = Flask(__name__)

calls = 0


@app.route("/requests", methods=['GET'])
def request_total():
    """
    :return: the total number of requests made to the service since most
    recent reboot as JSON
    """

    global calls
    calls += 1
    output = {"requests": calls}
    return jsonify(output)


@app.route("/classify", methods=['POST'])
def request_classify():
    """
    Takes in the image as JSON and coverts to nd array
    :return: JSON data of classification results
    """

    global calls
    calls += 1
    try:
        input = request.json['images']
    except:
        output = "Input data is not formatted correctly."
        return jsonify(output), 400
    try:
        output = {'classified': []}
        for image in input:
            # encode from unicode to utf-8, then decode to bytes
            im_data = base64.b64decode((image['data'].encode('utf-8')[2:-1]))
            # read as image data, save in ndarray
            im_data = np.array(Im.open(io.BytesIO(im_data)))
            # if >3 channel (e.g. png with transparency) drop it
            while np.shape(im_data)[2] > 3:
                im_data = im_data[:, :, :-1]
            raw_prediction = get_prediction(im_data)
            prediction = [raw_prediction[0],
                          np.ndarray.tolist(raw_prediction[1])]
            current_im_dict = {'name': image['name'], 'prediction': prediction}
            output['classified'].append(current_im_dict)

    except:
        output = "Internal Error"
        return jsonify(output), 500

    return jsonify(output)
