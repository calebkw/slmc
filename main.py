import platform
import os
from extract import extract
import api_send
from classification_output import write_to_file
from datetime import datetime


def start_classifier():
    """ Waits for image drive to be inserted, extracts files, submits API
    request, and writes results to classification.out.
    """

    while True:
        drive = input("Enter USB drive location or \'quit\' to exit: ").strip()
        if drive == 'quit':
            break
        elif hasdrive(drive):
            # extract images from drive
            try:
                image_array = extract(drive + ':')
                print('Images extracted: ' + str(len(image_array)))
            except SystemError:
                print('Image extraction from drive failed. Closing '
                      'program.')
                return
            # issue API request
            if len(image_array) > 0:
                try:
                    classified_array = api_send.classify(image_array)
                except:
                    print('API request for image classification failed. '
                          'Closing program.')
                    return
                # write output to file
                try:
                    for lesion in classified_array['classified']:
                        prob = lesion['prediction'][1][1]
                        if prob > 0.50:
                            outcome = lesion['prediction'][0][1]
                        else:
                            prob = lesion['prediction'][1][0]
                            outcome = lesion['prediction'][0][0]
                        write_to_file('classification.out', outcome, prob,
                                      lesion['name'], datetime.now().strftime(
                                       '%Y-%m-%d %H:%M:%S'))
                    print('Classifications sucessfully appended to '
                          '\'classification.out\'.')
                except:
                    print('Writing classifications to file failed. Closing '
                          'program.')
                    return
        else:
            print("No drive found at specified location.")


def hasdrive(letter):
    return "Windows" in platform.system() and os.system(
        "vol %s: 2>nul>nul" % letter) == 0


if __name__ == '__main__':
    start_classifier()
