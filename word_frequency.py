#!/usr/bin/env python3
import re
import string


def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True


# Function 1: validate sentence input
def get_sentence():
    while True:
        user_sentence = input("Enter a sentence: ")
        if is_sentence(user_sentence):
            return user_sentence
        else:
            print("This does not meet the criteria for a sentence.")


# Function 2: Calculate word frequencies
def calculate_frequencies(sentence):
    cleaned = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    words_list = cleaned.split()

    # Create parallel lists
    words = []
    frequencies = []

    for word in words_list:
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            words.append(word)
            frequencies.append(1)

    return words, frequencies


# Function 3: Print results
def print_frequencies(words, frequencies):
    print("\nWord frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


# Main controller function
def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)


# Run program
if __name__ == "__main__":
    main()

