# You can iterate through each letter of a string using either style of for-loop
# (the "for each" style or the "for i in range" style). For example, you can loop through
# each letter one at a time with the following code:

first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")

#out put is

# The letter is: B
# The letter is: r
# The letter is: i
# The letter is: g
# The letter is: h
# The letter is: a
# The letter is: m

#

print('\n\n')
#spacing

# Just as before, there is nothing special about the variable name letter,
# any name could have been used, but the choice of letter helps us keep the code nice and easy to read.


first_name = "Brigham"

fourth_letter = first_name[3] # Notice, using 3 instead of 4
print(fourth_letter) # outputs a 'g' on the screen

#
print('\n\n')
#spacing

word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    print(index)



#
print('\n\n')
#spacing

# Then, you can use the square brackets to access the letter at that index as follows:

word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")

# out put
# Index: 0 Letter: b
# Index: 1 Letter: o
# Index: 2 Letter: o
# Index: 3 Letter: k



#
print('\n\n')
#spacing


dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")

# out put

# What is your dog's name? Rover
# Your dog's name has 5 letters








# (Optional) Python Enumerate
# Using a for loop and the length of the string is a standard way to access both the index and the letter.
# However, Python also has a way to access both of these variables directly using a special function
# called enumerate as shown in the following example:


first_name = "Brigham"

# Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")
    
    
# The output of this code is:


# The letter B is at position 0
# The letter r is at position 1
# The letter i is at position 2
# The letter g is at position 3
# The letter h is at position 4
# The letter a is at position 5
# The letter m is at position 6


# This is a little different than the standard for loop, because it returns two variables.
# This function is not supported in many languages,
# but it is available in Python and you are welcome to use it in your programs if you would like.







# Printing without new lines
# To this point, whenever we have used a print statement,
# it has always been on it's own line, so that the next line starts on a new line. 
# If you do not want the print statement to end with a new line, you can specify the end as follows:


print("This is line one.", end="")
print("This is line two.")
# This outputs the following:


# This is line one.This is line two.


# Notice, that because you told the first print statement to end with nothing (by using ""),
# it does not end with a newline and the next line prints directly following it.




# Write a program that asks the user for their favorite letter.
# Then, loop through a programmed word one letter at a time.
# If the letter in the programmed word is the user's favorite,
# you'll first print it out as a capital letter, then later you will "hide" it.
# If the letter is not their favorite you will print it out as a lower case letter.



# The final version of this program will hide letters by turning them into an underscore _.
# To help you get to that point, you will work through three steps.




# Step 1
# Make the Favorite Letter uppercase
# Create a string variable to hold the word "Commitment".

# Write code that loops through the word letter by letter.
# If the letter is "m", print it as a capital letter.
# If the letter is anything else, print it out as a lowercase letter.

# For this part, it is ok to print each letter on it's own line.



#Step 2
# Clean up the Output
# Change the print statements so that each letter is not printed on its own line,
# but rather they are printed out next to each other on the same line.

# Also, change the program to allow the user to specify the letter
# (rather than always using "m"). Make sure your program matches the letter in the word,
# regardless of whether the user entered it as a capital or lowercase, and regardless of
# whether that letter was a capital or lowercase in the original word.


#Step 3
# Hide the Letter
# Change the program, so that instead of capitalizing the user's favorite letter,
# it "hides" it, and replaces it with an underscore in the display.


print('\n\n\n')
#spacing

word = "commitment"

favorite = input("What is your favorite letter? ")

###
# Steps 1 and 2
###
for letter in word:
 
    if letter.lower() == favorite.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

###
print('\n\n\n')# Core Requirement #3  plus spacing
###
for letter in word:
    if letter.lower() == favorite.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()
















"""
Author: Brother Burton
Purpose: Capitalizes letters in a string.
"""

word = "commitment"

favorite_letter = input("What is your favorite letter? ")

###
# Core Requirements #1 and #2
###
for letter in word:
    # Just in case the word or the user's letter contain a capital, we
    # should convert the letters to lowercase when we compare them
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

###
# Core Requirement #3
###
for letter in word:
    # Just in case the word or the user's letter contain a capital, we
    # should convert the letters to lowercase when we compare them
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()
