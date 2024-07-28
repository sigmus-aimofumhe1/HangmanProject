import random

# Get the words from the hangman_words list
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
