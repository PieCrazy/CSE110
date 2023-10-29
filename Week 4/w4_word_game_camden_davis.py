# This code is writen by Camden Davis for CSE110 week 4 Word game.
# This is a word game in the likes of wordle.
# I've listed the reqirements below.
#   GOING ABOVE AN BEYOND.
# I added explaniations to how this game is suppose to function. I also added lists of words
# that the game would choose from at the beginning to make the game fun for replayablility.
# I also added the ablity for the player to choose a catergory for the lsit of words to be chosen from.
 

"""
Here is the sources and the requirments.

                    Project Description
                    
The program contains a hidden secret word stored in a variable. 
This word can have any number of letters in it. When the program runs, 
the user is shown underscores ( _ ) for each letter of the word.

The user then enters a guess. If the guess is correct, the user wins and the game is over.

If the guess is not correct, the user will be given a hint to help them improve their
guess for the next round.

The game continues prompting the user for new guesses and showing them hints until 
they guess the word correctly. When the game is over, the program displays the number of
guesses that were made.

The guess must be the same number of letters as the secret word. 
If the guess has a different numbers of letters, the user is given a message explaining this,
and no hint is provided.

The hint shows the letters of the guess, but each letter is rendered in a special way as follows:

An underscore _ indicates that the letter was not present in the secret word.

A lowercase letter indicates that the letter was present somewhere in the secret word, 
but not at that position.

An uppercase letter indicates that the letter was present at that exact spot in the secret word. 
(In other words, if the second letter in the guess is also the second letter in the secret word, 
then that letter is shown as a capital.)





                 CODE REQUIRMENTS 
# 1 Have a secret word stored in the program.
#
# 2 Prompt the user for a guess.
#
# 3 Continue looping as long as that guess is not correct.
#
# 4 Calculate the number of guesses and display it at the end.
#
# 5 You do not need to have any hints at this point.
#
# 6 Use a loop to generate the initial hint.
#
# 7 Add a check to verify that the length of the guess is the same as the length of the secret word. 
#   If it is not, display a message. If they are the same, then proceed to give the hint.
#
# 8 Add the hints according to the rules above.
#
# 9 Make sure to account for the following in your hints:
#
# 10 Letters that are not present at all in the secret word (underscore _).
#
# 11 Letters that are present in the secret word, but in a different spot (lowercase).
#
# 12 Letters that are present in the secret word at that exact spot spot (uppercase).



#                    Showing Creativity and Exceeding Requirements
# Once you have the basic rules of the game in place, consider adding something extra to the hints, 
# other rules or limitations to the number of guesses, or anything else you think would be fun.
#
# If you want to look ahead at lists or files, you could start the game with a list of words, and select a random one for the secret word.




                                            SOURCES
# I added functions in general (I remembered how to do that or the basicas from c++ class i took)
# SHOWING CREDIT FOR LEARNING MORE ON PYTHON TO MAKE THE EXCEEDING THINGS TO WORK 
#
# SOURCES THAT I LEARNED STUFF ON WEEK ONE and two but will drop links just in case at this point.
# I've given credit as needed every time. don't want to get in trouble.
# not sure when its not neccisary to do these as 've learned them already.
#
#  I had to look up the clear terminal for python
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#
# I also wanted a time delay 
# https://realpython.com/python-sleep/
# i've learned and used this in every project for animation efffect or a natural pause feel.
#
#
#I looked ahead for the list, but i already knew how to do that when i wrote my restart function in week one.
#
lesson activty 3 of 3 this week had an optional part of enumerate.
        |
        v
# (Optional) Python Enumerate
# Using a for loop and the length of the string is a standard way to access both the index and the letter.
# However, Python also has a way to access both of these variables directly using a special function
# called enumerate as shown in the following example:


first_name = "Brigham"

# Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")
    

 
"""
import random
import time
import os
def main():  # The Main function calls varies functions
    intro()
    instructions()
def intro():
    print()
    print('Welcome to our Word Game Project.\n')
    print('This game is like wordle.')
    print()
    time.sleep(5)
    clear_screen()
def instructions():
    print('Here is how the game works in our instance.\n')
    print('The user then enters a guess. If the guess is correct, the user wins and the game is over.')
    print('If the guess is not correct, the user will be given a hint to help them improve theirguess for the next round.')
    print('The game continues prompting the user for new guesses and showing them hints until')
    print('they guess the word correctly. When the game is over, the program displays the number of\nguesses that were made.')    
    print('The guess must be the same number of letters as the secret word. ')
    print('If the guess has a different numbers of letters, the user is given a message explaining this,\nand no hint is provided. A guess is still counted though.')
    print('The hint shows the letters of the guess, but each letter is rendered in a special way as follows:')
    print('')
    print('An underscore _ indicates that the letter was not present in the secret word.')
    print('A lowercase letter indicates that the letter was present somewhere in the secret word,\nbut not at that position.')
    print('')
    print('An uppercase letter indicates that the letter was present at that exact spot in the secret word.')
    print('(In other words, if the second letter in the guess is also the second letter in the secret word,\nthen that letter is shown as a capital.)')
    print('')
    print('You will have 25 seconds to read this:')
    time.sleep(25)
    clear_screen()
    while True:
        restart_intro_tf =  'Would you like to see the instructions again?'  
        restart_intro_tf_a = input(f'{restart_intro_tf} (yes or no): ')
        restart_intro_tf_a = restart_intro_tf_a.strip().lower()
        if restart_intro_tf_a in ['yes', 'y']:
            print('One moement please.')   
            time.sleep(2)
            clear_screen()
            instructions()
        elif restart_intro_tf_a in ['no', 'n']:
            print()
            print('Perfect, we will continue on to our game then.')
            time.sleep(3)
            clear_screen()
            break
            
        else: 
            print(f'You may only input yes or no. You anserwed {restart_intro_tf_a} \n That is not a valid answer. Please try again.' )       
    word_list_selection()
def word_list_selection():
    global category_words
    category_words = []
    print()
    print('Please select a category from one of the following choices')
    print(' FRUITS      ANIMALS     SCRIPTURE-(books like JOHN)    SPORTS')
    select1 = input().strip().lower()
    #select1_c1 = select1_c1.strip().lower()
    select1_ans = 'no_answer'
    while select1_ans == 'no_answer':
        if select1 == 'fruits':
            print('\nYou have slected fruits for you category.\n\nGenerating a word now.')
            time.sleep(4)
            category_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
            select1_ans = 'answered'
            clear_screen()
        elif(select1 == 'animals'):
            print('\nYou have slected animals for you category.\n\nGenerating a word now.')
            time.sleep(4)
            category_words = ["cat", "dog", "tiger", "lion", "wolf", "fox", "bear", "zebra", "seal"]
            select1_ans = 'answered'
            clear_screen()
        elif(select1 == 'scripture'):
            print('\nYou have slected scripture for you category.\n\nGenerating a word now.')
            time.sleep(4)
            category_words = ["mosiah", "john", "moroni", "nephi", "matthew", "exodus", "alma"]
            select1_ans = 'answered'
            clear_screen()
        elif(select1 == 'sports'):
            print('\nYou have slected sports for you category.\n\nGenerating a word now.')
            time.sleep(4)
            category_words = ["football", "soccer", "baseball", "basketball", "hockey", "rugby", "tennis"]
            select1_ans = 'answered'
            clear_screen()
        else:
            print("That is not an acceptable answer! .")
            print('Please Type one of the following answers:\n FRUITS\nANIMALS\nSCRIPTURE-(books like JOHN)\nSPORTS ')
            select1 = input().strip().lower() 
    play_main_game()        
def play_main_game():  #This is the MAIN GAME LOGIC
    #looking at this i relized i was dumb and did extra.
    # # Pick a word from the catergory list slected before.
    # words = category_words
    # # Choose a random word from the list chosen before hand. grabbing that list from the global
    # secret_word = random.choice(words)
    
    #Choose a random word from the list or words chosen before habd in the previos function.
    secret_word = random.choice(category_words)

    # Initialize the guess count and the list of guessed letters
    guess_count = 0
    guessed_letters = []

    # Loop until the user guesses the word
    while True:
        # Print the current state of the word
        # THIS TOOOOOOK FOREVER TO FIGURE OUT
        
        #Let’s break it down:  I had to study the lists part of next week alot to figure this out honestly.

        # secret_word is the word that the user is trying to guess.
        # guessed_letters is a list of letters that the user has guessed so far.
        #
        # [c if c in guessed_letters else "_" for c in secret_word] is a list comprehension 
        # that creates a new list of characters. 
        # For each character c in secret_word, it checks if c is in guessed_letters.
        # If it is, then it adds c to the new list. Otherwise, it adds an underscore _.
        
        # " ".join(...) joins the list of characters into a string, separated by spaces.
        #
        # So the end result is a string that shows the current state of the word,
        # with underscores for unguessed letters and the actual letters for guessed letters.
        
        print(" ".join([c if c in guessed_letters else "_" for c in secret_word]))

        # Get a guess from the user and strip it to lower case so that the rest of the program behaves
        # (it didn't like it when it was all caps APPLES  and apples didn't give the same answer)
        guess = input("Enter your guess: ")
        guess = guess.strip().lower()
    
        # Check if the guess is valid 
        # it counts the guess letters and the words letters to see if they are the same mount.
        if len(guess) != len(secret_word):
            print("Your guess must be the same length as the secret word.")
            guess_count += 1
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
        
        #
        # Definition and Usage
        # The extend() method adds the specified list elements 
        # (or any iterable) to the end of the current list.
        # https://www.w3schools.com/python/ref_list_extend.asp
              
    restart_game()    
def clear_screen():  # Clear the Screen/terminal Function
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
def restart_game():   #restarts the game
            while True:
                restart_tf =  'Would you like to try again?'  
                restart_tf_a = input(f'{restart_tf} (yes or no): ')
                restart_tf_a = restart_tf_a.strip().lower()
                if restart_tf_a in ['yes', 'y']:
                    print()
                    print('One moment to restart')   
                    time.sleep(2)
                    clear_screen()
                    word_list_selection()
                elif restart_tf_a in ['no', 'n']:
                    clear_screen()
                    print()
                    print('Thank you for playing. Goodbye.')
                    time.sleep(3)
                    clear_screen()
                    exit()
                else: 
                    print(f'You may only input yes or no. You anserwed {restart_tf_a} \n That is not a valid answer. Please try again.' )              
if __name__ == '__main__':
     main()     