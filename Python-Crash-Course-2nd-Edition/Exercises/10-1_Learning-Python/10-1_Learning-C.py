file_path = '../../Working-With-Files/plain-file/fd-command.org'

with open(file_path) as file_object:
    file_lines_list = file_object.readlines()
    for line in file_lines_list:
        print(line.replace('fd', 'FIXME').strip())