def read_file(file_path):
    '''Reads the content of a file and returns it as a string.'''
    with open(file_path, 'r') as file:
        return file.read()

# Read data from the file called input.txt
