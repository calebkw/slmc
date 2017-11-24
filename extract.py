import os
#import lesion
import base64
import glob
import re
from Image import Image


def extract(dir):
    """ Extracts .jpg, .gif, png images from input directory, returns list of
    image objects
    :param: dir: directory in which image files are located
    """
    lesions = []
    dir = dir + "/*"
    for fname in glob.glob(dir):
        out = re.search('([^/]+\.(?:jpg|gif|png))', fname,
                        re.IGNORECASE)
        if out:
            with open(fname, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            new_lesion = Image(im_data=encoded_string, filename=
                               out.group(0))
            lesions.append(new_lesion)
    return lesions


if __name__ == '__main__':
    print(len(extract('C:/Users/Tim/Desktop/BMW USB/Europe 2016/*')))
