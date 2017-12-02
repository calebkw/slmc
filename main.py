import platform
import os
from extract import extract
from api_send import classify
from classification_output import write_to_file
from datetime import datetime


def start_classifier():
    """ Waits for image drive to be inserted, extracts files, submits API
    request, and writes results to file.
    """

    while True:
        drive = input("Enter USB drive location: ").strip()
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
                classified_array = classify(image_array)
            except SystemError:
                print('Image classification failed. Closing program.')
                return
            # write output to file
            try:
                for image in classified_array:
                    write_to_file('classification.out', image.output,
                                  image.filename, datetime.now().strftime(
                                   '%Y-%m-%d %H:%M:%S'))
            except SystemError:
                print('Writing classifications to file failed. Closing '
                      'program.')
                return
        else:
            print('NO DRIVE FOUND AT SPECIFIED LOCATION.')


def hasdrive(letter):
    return "Windows" in platform.system() and os.system(
        "vol %s: 2>nul>nul" % (letter)) == 0

