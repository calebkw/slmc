import os
#import lesion
import base64
import glob
import re


def extract(dir):
    lesions = []
    for fname in glob.glob(dir):
        if re.search('/([^/]+\.(?:jpg|gif|png))', fname, re.IGNORECASE):
            print(fname)
            with open(fname, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                lesions.append(encoded_string)
            '''
            new_lesion = lesion(encoded_string)
            lesions.append(new_lesion)
            '''
    return lesions


if __name__ == '__main__':
    print(len(extract('C:/Users/Tim/Desktop/BMW USB/Europe 2016/*')))
