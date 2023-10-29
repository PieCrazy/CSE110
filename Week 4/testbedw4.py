# animal = "rabbit"
# while animal == "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")

# c


# animal = "dog"
# while animal == "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")

#a
#b
#c

# animal = "dog"
# while animal != "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")

#C

# value = 10
# while value < 20:
#    value = value + 1
# print(value)

# 20

# while value < 20:
#    value = value + 1
# print(value)

#an error occours



# value = 20
# while value < 20:
#    value = value + 1
# print(value)

#20



import random

def main():
    play_game()

def play_game():
    # Define a list of words to choose from
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
        guess = input("Enter your guess: ")

        # Check if the guess is valid
        if len(guess) != len(secret_word):
            print("Your guess must be the same length as the secret word.")
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

        
        
