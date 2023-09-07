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


def main():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = int(input('Enter number of attempts: '))

    print("Welcome to field of dreams!")

    while True:
        print('\nСлово:', display_word(word_to_guess, guessed_letters))
        guess = input("Enter letter: ").lower()

        if guess in guessed_letters:
            print('You already guessed this letter')
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print(guess)
        else:
            attempts -= 1
            print('Failed')

        if '*' not in display_word(word_to_guess, guessed_letters):
            print('\nCongratulations! You win!')
            break

        if attempts == 0:
            print("Game over. Guessed word: ", word_to_guess)
            break



if __name__ == '__main__':
    main()