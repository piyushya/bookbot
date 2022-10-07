from collections import Counter
import string

file_path = "books/frankenstein.txt"
with open(file_path) as f :
    file_content = f.read()

def count_words(content) :
    words = content.split()
    return len(words)

def count_letters(content) :
    content = content.lower()
    cDict = {}
    for letter in string.ascii_lowercase :
        cDict[letter] = Counter(content)[letter]
    return cDict

def report() :
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(file_content)} words found in the document\n")
    for letter, count in count_letters(file_content).items() :
        print(f"The {letter} character was found {count} times")

report()
    

