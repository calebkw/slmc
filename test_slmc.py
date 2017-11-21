import shutil
import tempfile
from os import path


def test_write():
    """
    :Author: Tim Hoer
    :Date: November 20, 2017
    :Notes: Tests that write function writes image
    classifications to text file in specified directory.
    """
    #import function
    # create temporary directory
    test_dir = tempfile.mkdtemp()
    # call function
    write(temp_dir, array_of_image_objects)
    # check file
    f = open(path.join(test_dir, 'test.txt'))
    assert(f.read() is 'The owls are not what they seem')
    # remove temporary directory
    shutil.rmtree(test_dir)
    '''
    assert(os.path.isfile('ecg_data1_out.txt'))
    os.remove('ecg_data1_out.txt')
    '''


def test_mongo():
    """
    :Author: Tim Hoer
    :Date: November 20, 2017
    :Notes: Tests creation and access of MongoDB model instance.
    """
    #import MongoModel script
    #create instance
    #access instance



def test_extract():
    """
    :Author: Tim Hoer
    :Date: November 20, 2017
    :Notes: Tests that function loads all images from input directory and
    stores them as instances of the lesion class.
    """
    # import packages
    import os
    import urllib
    # import function, lesion class
    # create temporary directory
    test_dir = tempfile.mkdtemp()
    #test extract on empty directory
    assertRaises(Exception,extract,test_dir)
    # upload images to temporary directory
    fullfilename = os.path.join(test_dir, 'puppy.jpg')
    urllib.urlretrieve(
        "http://www.zarias.com/wp-content/uploads/2015/12/61-cute-puppies.jpg",
        fullfilename)
    fullfilename = os.path.join(test_dir, 'kitten.jpg')
    urllib.urlretrieve(
        "http://weknowyourdreams.com/images/kittens/kittens-02.jpg",
        fullfilename)
    # call function
    out = extract(test_dir)
    # check that output array is instance of lesion class
    assert(isinstance(out[0], lesion) is True)
    assert (len(out) == 2)
    # remove temporary directory
    shutil.rmtree(test_dir)


