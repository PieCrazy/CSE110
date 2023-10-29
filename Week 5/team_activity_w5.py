# Instructions
# Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.

# Once you have a list, have your program do the following:

# Core Requirements
# Work through these core requirements step-by-step to complete the program. 
# Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

# Compute the sum, or total, of the numbers in the list.

# Compute the average of the numbers in the list.

# Find the maximum, or largest, number in the list.

# Stretch Challenge
# Have the user enter both positive and negative numbers,
# then find the smallest positive number (the positive number that is closest to zero).

# Sort the numbers in the list and display the new, sorted list. 
# Hint: There are python libraries that can help you here, try searching the internet for them.
# import math
# numbers = []
# num = -23

# print('Enter numbers to enter into the list. type 0 when you have completed the numbers')
# while num != 0:
#     num = int(input('Please enter a number: '))
    
#     numbers.append(num)

# total = 0

# for num in numbers:
#     total += num

# print(f"You're total is {total}.")


# #average

# num_of_nums = len(numbers) - 1  # have to minus one because in testing we found it counted 0 in the average


# average = total / num_of_nums

# print(f"the average is {average:.2f}.")

# #maxnumber

# biggest_num = -350

# for num in numbers:
#     if num > biggest_num:
#         biggest_num = num
        
# print(f'Biggest number is: {biggest_num}')


numbers = []
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)

positive_numbers = [num for num in numbers if num > 0]
smallest_positive_number = min(positive_numbers, key=abs)

sorted_numbers = sorted(numbers)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Smallest positive number: {smallest_positive_number}")
print(f"Sorted numbers: {sorted_numbers}")