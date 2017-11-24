class Image:

    """Image class for holding image data and metadata"""

    def __init__(self, im_data, filename):
        """

        :param im_data: mxn array of image pixel data
        :param filename: str, name of file
        """

        self.image = im_data
        self.name = filename

'''
    def display(self):

        # display image?

    def size(self):
        numrows = len(self.image)
        numcols = len(self.image[0])

        return [numrows, numcols]
'''


