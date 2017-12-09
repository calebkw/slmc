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
                    request = api_send.classify(image_array)
                    classified_array = request[0]
                    status_code = request[1]
                except:
                    print('System server failure. Closing program.')
                    return
                # write output to file
                if status_code != 200:
                    print('API request for image classification failed. '
                          'Status code ' + str(status_code) + ".")
                else:
                    try:
                        for lesion in classified_array['classified']:
                            prob = lesion['prediction'][1][1]
                            if prob > 0.50:
                                outcome = lesion['prediction'][0][1]
                            elif lesion['prediction'][1][0] > 0.50:
                                prob = lesion['prediction'][1][0]
                                outcome = lesion['prediction'][0][0]
                            else:
                                prob = 1.00
                                outcome = 'indeterminate'
                            write_to_file('classification.out', outcome, prob,
                                          lesion['name'],
                                          datetime.now().strftime(
                                           '%Y-%m-%d %H:%M:%S'))
                        print('Classifications sucessfully appended to '
                              '\'classification.out\'.')
                    except:
                        print('Writing classifications to file failed. Closing'
                              ' program.')
                        return
        else:
            print("No drive found at specified location.")


def hasdrive(letter):
    return "Windows" in platform.system() and os.system(
        "vol %s: 2>nul>nul" % letter) == 0


if __name__ == '__main__':
    start_classifier()
