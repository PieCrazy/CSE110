# This code is writen by Camden Davis for CSE110 week 4 word game milestone

# i wrote the code for the main project first and then came back and made this work
# i took the basic part of it and made it work here.  all sources are in the finale not the milestone.

import random

def main():
    play_game()

def play_game():
    # List of words for this category. in the main project you can select whihc category you want to play from.
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    # Choose a random word from the list
    secret_word = random.choice(words)

    # Initialize the guess count and the list of guessed letters
    guess_count = 0
    guessed_letters = []

    # Loop until the user guesses the word
    while True:
        # Print the current state of the word
        print(" ".join([c if c in guessed_letters else "_" for c in secret_word]))

        # Get a guess from the user
        guess = input("Enter your guess:  (category fruits) ")
        guess = guess.strip().lower()
        # make all inputs lower case. APPLE and apple aren't the same and only lower case works.

        # Check if the guess is valid
        if len(guess) != len(secret_word):
            print("Your guess must be the same length as the secret word.")
            guess_count += 1 # if you guess wrong its still a guess!
            continue

        # Increment the guess count
        guess_count += 1

        # Check if the guess is correct
        if guess == secret_word:
            print(f"Congratulations! You guessed the word in {guess_count} guesses.")
            break

        # Generate a hint for the user
        hint = ""
        for i, c in enumerate(guess):
            if c == secret_word[i]:
                hint += c.upper()
            elif c in secret_word:
                hint += c.lower()
            else:
                hint += "_"
        print(f"Incorrect. Hint: {hint}")

        # Add the guessed letters to the list
        guessed_letters.extend(guess)
        
if __name__ == '__main__':
     main()     