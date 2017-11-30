import requests
import json


def classify(images_in):
    """

    :param images_in: list of Image objects
    :return:
    """

    # setup dict with empty list of image objects
    jsn_dict = {'images': []}

    for img in images_in:

        this_dict = {'name': img.name, 'data': img.data}
        jsn_dict['images'].append(this_dict)

    endpoint = 'http://vcm-1612.vm.duke.edu:5000/api/classify'

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(endpoint, data=json.dumps(jsn_dict), headers=headers)

    return r.json()


def num_requests():
    """Get total number of requests to server"""

    endpoint = 'http://vcm-1612.vm.duke.edu:5000/api/num_requests'

    r = requests.get(endpoint)

    return r.json()

