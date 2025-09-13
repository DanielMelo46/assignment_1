import os 

def read_file(file_path):
    '''Reads the content of a file and returns it as a string.'''
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    '''Writes the given content to a file.'''
    with open(file_path, 'w') as file:
        file.write(content)

def remove_spaces(text):
    chars_to_remove = [' ','\t','\n']
    for char in chars_to_remove:
        text = text.replace(char,"")
    return text

def word_list_gen(text):
    '''Generates a list of words from the text.'''
    word = [] # Stores characters of the current word
    splitted_words = [] # List to store all words
    for char in text:
        if char.isalpha(): # Only letters are part of words
            word.append(char)
        else:
            if word:  # Only append if word is not empty
                splitted_words.append(''.join(word))
                word = [] # Reset for the next word
    return [w.lower() for w in splitted_words if w]  


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

def most_common_words(text):
    ''' This function will count the occurrences of each word'''
    # counts = {} # Counts dictionary
    words = word_list_gen(text)
    # Calculate the word counts
    counts = {word : words.count(word) for word in set(words)}
    max_count = max(counts.values())
    # Find the most common words
    most_common = [word for word, count in counts.items() if count == max_count]
    return f'{', '.join(sorted(most_common))} ({max_count})'

def printer(file_content):
    """Creates a report of various statistics about the text.

    Args:
        file_content (str): The content of the file to analyze.
    """
    return (
        f'Word count: {word_count(file_content)}\n'
        f'Unique words: {unique_words(file_content)}\n'
        f'Characters (with spaces): {characters_with_spaces(file_content)}\n'
        f'Characters (no spaces): {characters_without_spaces(file_content)}\n'
        f'Average word length: {avg_word(file_content)}\n'
        f'Most common word(s): {most_common_words(file_content)}'
    )

# Read data from the file called input.txt
def main():
    for i, file in enumerate(list(os.listdir('inputs'))):
        # Read the content of the file
        file_content = read_file(f'inputs/{file}')
        report = printer(file_content)
        # Write the report to an output file
        write_file(f'outputs/output_{i + 1}.txt', report)
        print(f'output_{i + 1}.txt: \n{report}\n')

#Execution
main()
