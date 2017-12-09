import platform
import os
from extract import extract
import api_send
from classification_output import write_to_file
from datetime import datetime


def start_classifier():
    """ Waits for image drive to be inserted, extracts files, submits API
    request, and writes results to file.
    """

    while True:
        drive = input("Enter USB drive location or \'quit\' to exit: ").strip()
        if drive == 'quit':
            break
        elif hasdrive(drive):
            # extract images from drive
            try:
                image_array = extract(drive + ':')
                print('Extracted images: ' + str(len(image_array)))
            except SystemError:
                print('Image extraction failed. Closing program.')
                return
            # issue API request
            if len(image_array) > 0:
                try:
                    classified_array = api_send.classify(image_array)
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
                    print('Classifications sucessfully appended to '
                          '\'classification.out\'.')
                except SystemError:
                    print('Writing classifications to file failed. Closing '
                          'program.')
                    return
        else:
            print("No drive found at specified location.")

def hasdrive(letter):
    return "Windows" in platform.system() and os.system(
        "vol %s: 2>nul>nul" % (letter)) == 0


if __name__ == '__main__':
    start_classifier()
