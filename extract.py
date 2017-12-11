import base64
import glob
import re
from Image import Image


def extract(directory):
    """ Extracts .jpg images from input drive, returns list of
    image objects
    :param: dir: directory in which image files are located
    """
    lesions = []
    directory = directory + "/*"
    for fname in glob.glob(directory):
        out = re.search('([^/]+\.(?:jpg|jpeg|png))', fname,
                        re.IGNORECASE)
        if out:
            with open(fname, "rb") as image_file:
                encoded_string = str(base64.b64encode(image_file.read()))
            new_lesion = Image(im_data=encoded_string, filename=
                               out.group(0))
            lesions.append(new_lesion)
    return lesions


if __name__ == '__main__':
    extract('C:/Users/Tim/Desktop/BMW USB/Europe 2016')
