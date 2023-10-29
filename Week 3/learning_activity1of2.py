# # Attempt 1 more words
# price = float(input('What is the price?'))
# if price >= 1.00:
#     tax = .07  
#     print(tax)
# else:
#     tax =0
#     print(tax)
#     #  > greater than
#     #  < less than
#     # >= greater tjam or equal to
#     # <= less than or equal to
#     # == is equal to
#     # != is not equal to 
    
# # attempt 2

# if price >= 1.00:
#     tax2 = .07
# else:
#     tax2 = 0
# print(tax2)


# # both do the same attempt 2 is more elequant    



# #compareing strings is hard and can get you into trouble
# # this below shows why
# #strings are case sensitve.

# country = 'CANADA'
# if country == 'CANADA':
#     print('Oh look a Canadian')
# else:
#     print('You are not from Canada')
    
# # to do this right you would need to format the inputs

# country = 'Canada'
# if country.lower() == 'canada':  #like this
#         print('Oh look a Canadian')
# else:
#     print('You are not from Canada')
    
# price = input('how much did you pay? ')
# price = float(price) 

# that can be done in one line like this




# price = float(input('how much did you pay? '))
# # if price >= 1.00:
# #     tax = .07
# #     print('Tax rate is: ' + str(tax))
# # else:
# #     tax = 0
# #     print('Tax rate is: ' + str(tax))
 
 
    
# #THis is the same
# if price >= 1.00:  
#     tax = .07
    
# else:
#     tax = 0
# print('Tax rate is: ' + str(tax))  
    
    
# #nesting if state ments

# or statemetns

# in  for lists

# Activity Instructions
# Practice writing programs that compare strings and numbers.

# Comparing Numbers
# Write a program that asks the user for two integers.

# Then, write three separate if/else statements as follows:

# If the first number is greater than the second,
#   print "The first number is greater".
#   Otherwise, print "The first number is not greater".

# If the two numbers are equal print "The numbers are equal".
#   Otherwise, print "The numbers are not equal".

# If the second number is greater than the first, 
# print "The second number is greater".
#   Otherwise, print "The second number is not greater".

#Have the program ask the user for their favorite animal. Then write an if statement as follows:

# What is the first number? 4
# What is the second number? 3
# The first number is greater
# The numbers are not equal
# The second number is not greater

# What is your favorite animal? giraffe
# That one is not my favorite.

#Then, write three separate if/else statements as follows:

first_num = int(input('What is the first number? '))
second_num = int(input('What is the second number? '))
if first_num > second_num:
    print('The first number is greater')
else:
    print('The first number is not greater')
if first_num == second_num:
    print('The numbers are equal')
else:
    print('The numbers are not equal')
if first_num < second_num:
    print('The second number is greater')
else:
    print('The second number is not greate')
print()# spacing

cam_fav_animal = 'cat'
user_fav_animal = input('What is your favorite animal? ')
if user_fav_animal.lower() == cam_fav_animal:
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite')

#works



# Testing Procedure
# Verify that your program works correctly by following each step in this testing procedure:

# Test the first part of your program with pairs of numbers where the first is greater and also where the second is greater. Verify that all three values that are printed are correct.

# Test it with two numbers that are equal. Verify that all three values that are printed are correct.

# Test the second part of your program with an animal that is different. Verify that the correct message is shown.

# Test it with an animal that is the same. Verify that the correct message is shown.

# Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.