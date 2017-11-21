import os
#import lesion
import base64
import glob
import re


def extract(dir):
    lesions = []
    for fname in glob.glob(dir):
        print(fname)
        print(re.search('(?i)\.(jpg|png|gif)$/i', fname))
        if re.search('(?i)\.(jpg|png|gif)$/i', fname):
            print(fname)
            with open(fname, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())

            '''
            new_lesion = lesion(encoded_string)
            lesions.append(new_lesion)
            '''
    return lesions


if __name__ == '__main__':
    extract('C:/Users/Tim/OneDrive/Pictures/Screenshots/*')
