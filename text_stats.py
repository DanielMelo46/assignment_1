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
    chars_to_remove = [' ','\t','\n']
    for char in chars_to_remove:
        text = text.replace(char,"")
    return text

def word_list_gen(text):
    '''Generates a list of words from the text.'''
    words = remove_char(text).split(" ")
    return [word.lower() for word in words]

def word_count(text):
    '''Counts the number of words in the text.
    It uses the remove_char function to clean the text first.'''
    words_list = word_list_gen(text)
    return len(words_list)

def unique_words(text):
    '''Returns a set of unique words from the text.'''
    words_list = word_list_gen(text)
    return len(set(words_list))

def characters_with_spaces(text):
    '''Returns the number of characters in the text, including spaces.'''
    return len(text)

def characters_without_spaces(text):
    return len(remove_spaces(text))

def avg_word(text):
    all_words = word_list_gen(text)
    all_words_join = ''.join(all_words) 
    # Counting all the letters in the text
    total_letters = sum(1 for char in all_words_join if char.isalpha()) 
    return f'{total_letters / word_count(text):.1f}'

# def most_common_words(text):
#     ''' This function will count the occurrences of each word'''
#     counts = {} # Counts dictionary
#     words





# Read data from the file called input.txt
# Read it into a variable
file_content = read_file('inputs/input_1.txt')
print(avg_word(file_content))

