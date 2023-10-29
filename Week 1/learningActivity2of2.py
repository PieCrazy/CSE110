


#This is the first part of video  im doing this so i can section
#out this part of teh code and not have conflicting variables. 


#first_name = 'Camden'
#last_name = 'Davis'
#print(first_name + last_name)
#print('Hello ' + first_name + ' ' + last_name)
# this is from the beginning of video 9 of 44


#from latrer in the video

#sentence = 'The dog is named Sammy '
#print(sentence.upper())
#print(sentence.lower())
#print(sentence.capitalize())
#print(sentence.count('a'))
#  later in the viedo

# video 10 of 44
#first_name = input('What is your first name? ')
#last_name = input('What is your last name? ')
#print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

#video 11 and 12 of 44
#format strings

#first_name = 'Camden'
#last_name = 'Davis'
#output = 'Hello, ' + first_name + ' ' + last_name
#output = 'Hello, {} {}'.format(first_name, last_name)
#output = 'Hello, {0} {1}'.format(first_name, last_name)
#output = f'Hello, {first_name} {last_name}'
#print(output)

"""
Instructions
Prompt the user for their first name. Then, prompt them for their last name. Display the text back all on one line saying, "Your name is last-name, first-name, last-name" as shown:


examples

What is your first name? Scott
What is your last name? Burton

Your name is Burton, Scott Burton.

What is your first name? Brigham
What is your last name? Young

Your name is Young, Brigham Young.
    
    
Make sure to be precise! You should have the spacing, comma, and period appear exactly as shown in the examples.

Adjust the Capitalization
Now that the program is displaying the strings back with the correct spacing, improve your program by making it display the words using the .title() function on each variable so that it capitalizes only the first letter and all the other letters are lowercase.

Test that your program works by trying some words that are capitalized and some that are lower case. The output should be the same. For example: 



What is your first name? Brigham
What is your last name? Young

Your name is Young, Brigham Young.

What is your first name? brigham
What is your last name? YOUNG

Your name is Young, Brigham Young.

What is your first name? brIGham
What is your last name? YOUng

Your name is Young, Brigham Young.   
    
"""


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# ADJSUMTNETS
#
# print('Your name is ' + last_name.capitalize + ', ' + first_name.capitalize + last_name.capitalize)
# 
# this didn't work
#
# output = f'Your name is {last_name.capitalize}, {first_name.capitalize} {last_name.capitalize}.'
# this didnt work either
#
# output = f'Your name is {last_name}, {first_name} {last_name}.'
#
# This worked except the capitals but i relised i forgot thr () after the capilize
# 
# output = f'Your name is {last_name.capitalize()}, {first_name.capitalize()} {last_name.capitalize()}.'
#
# WORKED YAY
output = f'Your name is {last_name.title()}, {first_name.title()} {last_name.title()}.'
print(output)


