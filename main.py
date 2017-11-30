import platform
import os
from extract import extract


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

            # write output to file



def hasdrive(letter):
    return "Windows" in platform.system() and os.system(
        "vol %s: 2>nul>nul" % (letter)) == 0

if __name__ == '__main__':
    print(start_classifier())
