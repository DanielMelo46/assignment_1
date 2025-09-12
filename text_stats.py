
def read_file(file_path):
    '''Reads the content of a file and returns it as a string.'''
    with open(file_path, 'r') as file:
        return file.read()
    
def remove_char(text):
    chars_to_remove = [',','.','\n']
    for char in chars_to_remove:
        text = text.replace(char,"")
    return text

#def word_count(text):
    
# Read data from the file called input.txt
# Read it into a variable
file_content = read_file('inputs/input_1.txt')
print(file_content)
print(remove_char(file_content))



