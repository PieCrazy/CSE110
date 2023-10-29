
# Instructions
# In the Guess My Number game the computer picks a magic number, and then the user tries to guess it.
# After each guess, the computer tells the user to guess "higher" or "lower" until they guess the magic number.

# This assignment is a little tricky, because it brings together many of the concepts you've learned in this course 
# including loops and if statements.

# Having the computer pick a random number
# There is a random number library included with Python that contains a number of 
# different functions to generate random numbers, depending on if you want integers, floating point numbers,
# and from different statistical distributions.

# The only function you will need from this library is called randint. To use it, you give it two numbers 
# and it returns back a random number in that range. In order to use this function you need to import
# it from the random library.

# The following code shows how to import the function and use it to get a random number from 1 to 10.

#core 1

# Start by asking the user for the magic number.
# (In future steps, we will change this to have the computer generate a random number,
# but to get started, we'll just let the user decide what it is.)

# Ask the user for a guess.

# Using an if statement, determine if the user needs to guess
# higher or lower next time, or tell them if they guessed it.

#core 2

# Add a loop that keeps looping as long as the guess does not match the magic number.

# At this point, the user should be able to keep playing until they get the correct answer.

#core 3

# Instead of having the user supply the magic number, import the random library and use it to generate a random number from 1 to 100.

# Play the game and make sure it works!


#core

# import random

# the_numberc = random.randint(1, 100)


# guessc = 300 # making a negative number or a number larger than 100 so that the random
#            #doesn't accidently choose our number 

# # Keep going as long as the guess doesn't match the magic number
# while guessc != the_numberc:
#     guessc = int(input("What is your guess? "))

#     if guessc < the_numberc:
#         print("Higher")
#     elif guessc > the_numberc:
#         print("Lower")
#     else:
#         print("You guessed it!")
        
        
        
        
# #STRECH

# Keep track of how many guesses the user has made and inform them of it at the end of the game.

# After the game is over, ask the user if they want to play again. 
# Then, loop back and play the whole game again and continue this loop as long as they keep saying "yes".

import random
continue_playing = "yes"
while continue_playing == "yes":
    magic_number_s = random.randint(1, 100)
    num_of_guesses = 0
    guess_s = 300  #cant have it be in our range of numbers but it needs a value
    
    while guess_s != magic_number_s:
        guess_s = int(input("Guess a number: "))
        num_of_guesses = num_of_guesses + 1
        
        if guess_s < magic_number_s:
            print('guess higher')
        elif guess_s > magic_number_s:
            print('guess lower')
        else: 
            print('Right on you got it!')
    
    print(f'You took {num_of_guesses} guesses to fianlly get it')
    
    continue_playing = input('Try again? (yes/no)? ')
    
print('good bye.')