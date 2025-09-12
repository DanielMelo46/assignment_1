def read_file(file_path):
    '''Reads the content of a file and returns it as a string.'''
    with open(file_path, 'r') as file:
        return file.read()

# Read data from the file called input.txt
file_content = read_file('inputs/input_1.txt')
print(file_content)
# Read it into a variable


