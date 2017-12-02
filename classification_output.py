def write_to_file(output_filename, classified_output, image_filename, date):
    """ Writes the output to a seperate file
    :param output_filename: str,name for output
    :param classified_output: The classification of the output file
    :param image_filename: Unique patient identifier
    :param date: Date when the request for classification was made

    """

    file = open(output_filename, 'w')
    file.write('image: ')
    file.write(str(image_filename))
    file.write(', ')
    file.write('classification: ')
    file.write(str(classified_output))
    file.write(', ')
    file.write('date: ')
    file.write(str(date))
    file.write("\n")
    file.close()

    file.close()


