 #This code is writen by Camden Davis for CSE110 week 2 project Meal Price Calculator  project milestone.
 
#I wrote this as a seprate program from my project as I've already gotten far, and changed the program for the 
# showing creativity requirements

 #Milestone Requirements:
#By midweek, to help make sure you are on track to finish the assignment, you need to complete the following:

#1.Ask the user for the price of a child and an adult meal and store these values properly into 
# variables as floating point numbers.

#2.Ask the user for the number of adults and children and store these values properly
# into variables as integers.

#3.Compute and display the subtotal (you do not need to worry about the sales tax or rounding to two
# decimals at this point).

print('Mid Week Milestone.')
meal_child = float(input("What is the price of a child's meal? ")) #using "blah " because of the ' in child's
meal_adult = float(input("What is the price of an adult's meal? "))# same but Adult's
num_child_meal = int(input('How many children are there? '))
num_adult_meal = int(input('How many adults are there? '))
print() #Spaceing 
subtotal = (num_adult_meal * meal_adult ) + (num_child_meal * meal_child)
print(f'Subtotal:{subtotal:.2f}')
# Displays the subtotal with 2 decimal places of percision.
#Doesn'tincude the currency but that isn't required for this
#
# Completes All requirements for the mid week milestone Challenge