file_path = '../../Working-With-Files/plain-file/fd-command.org'

with open(file_path) as file_object:
    # # Reading in the entire file
    # content = file_object.read()
    #
    # # Looping through the file object
    # for line in file_object:
    #     print(line.strip())

    # Storing the lines in a list
    file_lines_list = file_object.readlines()
    for line in file_lines_list:
        print(line.strip())

# Reading in the entire file.
# print(content)