'''
INSTRUCTIONS TO REFER TOO

Overview
An ID badge, such as a drivers license or student ID, contains personal details that are formatted in a very specific way.

For this activity you will write a program that will create a properly formatted ID badge.

Assignment
Write a program to prompt the user for the following:

First name

Last name

Email Address

Phone Number

Job Title

ID Number

Then you should display the information back in this format:

Note that the square brackets [] indicate a value coming from the user and should not be displayed.


----------------------------------------
[LAST NAME], [first name]
[Job title]
ID: [id number]

[email address]
[phone number]
----------------------------------------



In addition to the spacing and punctuation shown above, you must implement the following requirements:

The last name should be converted from whatever the user types to be displayed in ALL CAPS.

The job title should be displayed so that the first letter is capitalized.

The email address should be displayed in all lowercase.

An example of the program running is shown:


Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------





Core Requirements
Each team activity will contain three core requirements. These are items that you are expected to be able to complete during the one hour team meeting if you have come prepared.

You should work through the assignment in this order:

Prompt for all of the necessary values and store them in variables. Then display each item to the screen, without worrying about any spacing, punctuation, or formatting yet.

Arrange the display so that the spacing and punctuation exactly match the example shown.

Use the built-in string functions to make the last name display in all caps, the job title display in "title case," and the email display in all lowercase.

Stretch Challenge
Most team activities will also contain stretch challenges, which are not specifically required by the assignment, but are a great way to dive deeper into the material. They can be more difficult and may require you to find solutions that weren't directly covered in the preparation material.

The stretch challenges for this activity are:

Add hair color and eye color and put them both on the same line in the display.

Add a field for the name of the month they started and also a yes/no field for whether they have completed advanced training. Put these both on the same line in the display.

For the two lines that you just added, make it so that the second columns align, regardless of how many letters are in the responses.

To complete this one, you may need to search the internet for something like, "python spacing format" or something similar to see if you get any ideas.

At the end of the stretch challenge, your output should look something like the following:


The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234

Hair: Brown           Eyes: Blue
Month: September      Training: Yes
----------------------------------------

'''
# Code Writen By Camden Davis 
# Using the above instructions for CSE110 week 1 activity.
# My ACtual Code now that i have read through the instructions and what is being asked of me.

print('Please enter the folowing information: ')

print()
#all the prmpts

first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone_number = input('Phone number: ')
job_name = input('Job title: ')
id_num = input('ID number: ')
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
start_month =input('What month did you start? ')
training = input('Yes or no, have completed advanced training? ')
border = '----------------------------------------'

# creating space from the questions with print function of blank so thath the terminal isn't messy when you try to see what
# it is going to print for the ID after all the questions

print()
print()
print()

# that was the space i was talking about in th terminal.

print('The ID Card is: ')
print(border)
#name = f" {last_name.capitalize()} {', ' } {first_name.capitalize()}"
#This code above printed  Last , First
#also relized i need  to make the last name display in all caps.
name = (last_name.upper() + ', ' + first_name.capitalize())
#This Code printed name like  LAST, First
print(name)
print(job_name.title())
print('ID: ' + id_num)
print()
print(email.lower())
print(phone_number)
# if i add print border here that is the core challeneg complete.
# below is the remining code for the stretch challenge
# https://stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings
# used this to learn or try to align

print()
print(('Hair: ' + hair_color + '\t' + 'Eyes:' + eye_color).expandtabs(20))
print(('Month:' + start_month + '\t' + 'Training: ' + training).expandtabs(20))
print(border)

# learned about the expand tabs from that and it was nice!