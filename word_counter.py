import re
from collections import Counter
import os
print(os.getcwd())

# function to read a text file and return its contents as a string
def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents

# function to split the contents of a file into words
def split_into_words(contents):
    words = re.findall(r'\b\w+\b', contents.lower())
    return words

# function to count how often each word occurs in a list of words
def count_words(words):
    word_counts = Counter(words)
    return word_counts

# function to display the word counts
def display_word_counts(word_counts):
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# main function
def main(file_path):
    contents = read_file(file_path)
    words = split_into_words(contents)
    word_counts = count_words(words)
    display_word_counts(word_counts)

if __name__ == '__main__':
    main('sample_text_file.txt')