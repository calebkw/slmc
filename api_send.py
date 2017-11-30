import requests
import json
import numpy as np


def classify(image):
    """

    :param image: Image object
    :return:
    """

    # extract and encode to string if not already done
    data = image.data

    jsn = {'image': image}
    endpoint = 'http://vcm-1612.vm.duke.edu:5000/api/classify'

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(endpoint, data=json.dumps(jsn), headers=headers)

    return r.json()


def num_requests():
    """Get total number of requests to server"""

    endpoint = 'http://vcm-1612.vm.duke.edu:5000/api/num_requests'

    r = requests.get(endpoint)

    return r.json()