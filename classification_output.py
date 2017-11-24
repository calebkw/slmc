def write_to_file(output_filename, classified_output , UUID, Date)
    """ Writes the output to a seperate file

    :param: output_filename: str,name for output
    :param classified _output: The classification of the output file
    :param: UUID: The Unique ID for each patient
    :param: Date: Date when the request for classification was made

    """
    import output

    file = open(output_filename, 'w')
    file.write('The image is classified as:')
    file.write(str(classified_output))
    file.write("\n")
    file.write('The UUID for the image is:')
    file.write(str(UUID))
    file.write("\n")
    file.write('The dtae of request is:')
    file.write("\n")
    file.close()


