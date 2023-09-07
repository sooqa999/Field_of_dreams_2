import random


def choose_word():
    words = ['apple', 'peach', 'strawberry']
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '*'
    return display

