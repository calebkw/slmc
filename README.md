# slmc 
Classifies the input Melanoma images from the user as either being malignant or benign.



The Software License for the file is:
=========
LICENSE.md ( MIT License)

The Travis Badge is:
=========
[![Build Status](https://travis-ci.org/calebkw/slmc.svg?branch=master)](https://travis-ci.org/calebkw/slmc)

Read the Docs Badge:
=========
<a href='http://slmc.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/slmc/badge/?version=latest' alt='Documentation Status' />
</a>   


Starting the Program
=========
The program may be started by running main.py. Users running Windows may then specify either the directory or the drive letter from which to extract skin lesion images. On Linux, the program will detect a USB connected to any of the USB ports and then prompt the user if they would like to specify a subdirectory on the drive from which to extract images (this functionality is intended for use with a Raspberry Pi client). Mac users will simply be prompted to enter the directory from which to extract images. Typing quit for this prompt will end the program.

Requirements:
=========
Python 3.5

Windows/Mac: Any file directory containing skin lesion images.
Linux: Removable media drive with the images to be classified.
Optional: Raspberry Pi client

Output
=========
The output is printed to classifications.out and is written to the drive or directory containing the extracted images.

Each line contains the image filename, the classification, and the date separated by commas.


Unit Testing
=========
Unit testing is performed using py.test by running test_slmc.py.


Additional Files
=========
Additional files are provided in the 'submission' folder. This folder contains an overview and performance evaluation of the service is provided in 'overview.pdf'. This folder also contains our RFC document and video demonstrations of running the program locally as well as on the Raspberry Pi client via SSH. 

A pip3 virtual environment containing all dependencies is located in the 'pi_env' folder. An environment.yml file for creating a virtual environment with conda is located in the main directory.


Team Members:
======
+ Caleb Willis
+ Tim Hoer
+ Mounika Vanka


Credits
=======
* Mark Palmeri
* Suyash Kumar
* Arjun Desai


