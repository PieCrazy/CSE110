# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the
# number is negative, then display the number. 
# For example:

# Please type a positive number: -3
# Sorry, that is a negative number. Please try again.
# Please type a positive number: -8
# Sorry, that is a negative number. Please try again.
# Please type a positive number: -1
# Sorry, that is a negative number. Please try again.
# Please type a positive number: 12
# The number is: 12

# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you." For example:


# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? no
# May I have a piece of candy? yes
# Thank you.


possitve_number = float(input('Please type a positive number. '))

while possitve_number <= 0:
     print('Please try again.')
     possitve_number = float(input('Please type a positive number. '))
print(f'The number is: {possitve_number:.2f}')

#while answer != "yes":     man i forgot about !=
candy = 'no'

while candy == "no":
    candy = input("May i have a piece of candy? ")
print('Thank you')


    
