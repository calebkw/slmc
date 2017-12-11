def test_extract():
    """
    :Author: Tim Hoer
    :Date: November 20, 2017
    :Notes: Tests that function loads all images from input directory and
    stores them as instances of the lesion class.
    """
    import os
    import urllib.request
    import shutil
    import tempfile
    from extract import extract
    from Image import Image
    # create temporary directory
    test_dir = tempfile.mkdtemp()
    # upload images to temporary directory
    fullfilename = os.path.join(test_dir, 'puppy.jpg')
    urllib.request.urlretrieve(
        "http://www.zarias.com/wp-content/uploads/2015/12/61-cute-puppies.jpg",
        fullfilename)
    fullfilename = os.path.join(test_dir, 'kitten.jpg')
    urllib.request.urlretrieve(
        "http://weknowyourdreams.com/images/kittens/kittens-02.jpg",
        fullfilename)
    # call function
    out = extract(test_dir)
    # check that output array is instance of lesion class
    assert (len(out) == 2)
    assert(isinstance(out[0], Image) is True)
    # remove temporary directory
    shutil.rmtree(test_dir)


def test_write():
    """
    :Author: Tim Hoer
    :Date: November 20, 2017
    :Notes: Tests that write function writes image
    classifications to text file in specified directory.
    """
    import shutil
    import tempfile
    from os import path
    from classification_output import write_to_file
    # create temporary directory
    temp_dir = tempfile.mkdtemp()
    # call function

    write_to_file('test.txt', temp_dir, 'high risk', '.50',
                  'patient10.jpg', '6/9/69')
    # check file
    f = open(path.join(temp_dir, 'test.txt'))
    assert(f.read() == 'image: patient10.jpg, classification: high risk, '
                       'certainty: .50, date:'
                       ' 6/9/69\n')
    # close file
    f.close()
    # remove temporary directory
    shutil.rmtree(temp_dir)
