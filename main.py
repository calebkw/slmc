import platform
import os
from extract import extract
import api_send
from classification_output import write_to_file
from datetime import datetime
import json


def start_classifier():
    """ Waits for image drive to be inserted, extracts files, submits API
    request, and writes results to file.
    """

    drive = input("Enter USB drive location: ").strip()
    while True:
        if hasdrive(drive):
            print('DRIVE INSERTED')
            # extract images from drive
            try:
                image_array = extract(drive + ':')
                print('IMAGES EXTRACTED: ')
                print(len(image_array))
            except SystemError:
                print('Image extraction failed. Closing program.')
                return
            # issue API request
            try:
                classified_array = api_send.classify(image_array)
                #classified_array = api_send.num_requests()
            except SystemError:
                print('Image classification failed. Closing program.')
                return
            # write output to file
            try:
                for dict in classified_array['classified']:
                    prob = dict['prediction'][1][1]
                    if prob > 0.50:
                        outcome = dict['prediction'][0][1]
                    else:
                        outcome = dict['prediction'][0][0]
                    write_to_file('classification.out', outcome,
                                  dict['name'], datetime.now().strftime(
                                   '%Y-%m-%d %H:%M:%S'))
            except SystemError:
                print('Writing classifications to file failed. Closing '
                      'program.')
                return


def hasdrive(letter):
    return "Windows" in platform.system() and os.system(
        "vol %s: 2>nul>nul" % (letter)) == 0


if __name__ == '__main__':
    start_classifier()
