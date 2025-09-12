def read_file(file_path):
    '''Reads the content of a file and returns it as a string.'''
    with open(file_path, 'r') as file:
        return file.read()
    
def remove_char(text):
    '''Removes specific characters from the text.'''
    chars_to_remove = [',','.','\n']
    for char in chars_to_remove:
        text = text.replace(char,"")
    return text

def remove_spaces(text):
    chars_to_remove = ['\s','\t','\n']
    for char in chars_to_remove:
        text = text.replace(char,"")
    return text

def word_count(text):
    '''Counts the number of words in the text.
    It uses the remove_char function to clean the text first.'''
    words_list = remove_char(text).split(" ")
    return len(words_list)

def unique_words(text):
    '''Returns a set of unique words from the text.'''
    words_list = remove_char(text).split(" ")
    return len(set(words_list))

def characters_with_spaces(text):
    '''Returns the number of characters in the text, including spaces.'''
    return len(text)

#def characters_without_spaces(text):




# Read data from the file called input.txt
# Read it into a variable
file_content = read_file('inputs/input_1.txt')
print(characters_with_spaces(file_content))

