#Learning Activity (2 of 2): Mathematical Expressions

#Write a program to convert from Fahrenheit to Celsius. Display the
# result to one decimal place of precision.
# To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount 
# and then multiply it by the fraction 5/9.

#The colon (:) after the variable name indicates that you are going to specify how to format it.
#The period (.) indicates that you are setting the precision or number of decimal places.
#The number (in this example 2) indicates that you would like that number of decimal places to be displayed
#The f indicates that you want fixed-point notation.

#Written By Camden Davis

tempf = input('What is the temperature in Fahrenheit? ')
tempc = (float(tempf) - 32) * (5/9) 
# It took a minute to get the () set up correctly
print(f'The temperature in Celsius is {tempc:.1f} degrees.')

# Prints the correct conversion and to one dewcimal place of percision.