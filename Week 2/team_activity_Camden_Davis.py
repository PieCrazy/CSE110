
"""
    #Assignment
# Start by completing the core requirements. Then, when that part is complete,
# if you have time, see if you can complete some of the stretch challenges as well.

# Core Requirements
#Write a program to compute the areas of three different shapes. Prompt for the necessary information,
# then compute and display the area, as follows:

#Make sure that your program can appropriately handle decimal values as well as whole numbers.

# 1.Square—The area is the length of a side squared.

# 2.Rectangle—The area is the length multiplied by the width.

# 3.Circle—The area is Pi (you can use 3.14) multiplied by the radius squared. 

# Stretch Challenge
# Once you have finished the core requirements, you are welcome to move on to the stretch challenges.
# These can be more difficult and may require finding solutions that weren't directly covered in the reading. 
# These aren't specifically required for the assignment, but are a great chance to dive deeper into the
# concepts of the lesson.

# The stretch challenges for this activity are:

# 1 Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included
#   in the python "math" module. Hint, you might try searching on the internet for something like,
#   "python how to get the value of pi."

# 2 Prompt the user for a single length value, then compute and display the areas of a square with that 
#   length of side, a circle with that radius, and then the volumes of a cube with that side and 
#   a sphere with that radius, all from the same value from the user.

# 3 For each of the three areas in the core requirements, change the prompt for the user to ask for the value 
#   in centimeters. Then, display the resulting area in both square centimeters and square meters.
#   Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.
    """
#Code Writen By Camden Davis for CSE110

#CORE Challenge atempt by camden
print('Core challenges for square, rectangle, and circle with no fancy operations')
square = float(input('What is the length of the side of the square? '))
print(f'The area of the square is: {square * square}')
#Works as expected.
rectangle_l = float(input('What is the length of the rectangle? '))
rectangle_w = float(input('what is the width of the rectangle? '))
print(f'The area of the rectangle is: {rectangle_l * rectangle_w}')
#works as expected
circle_r =float(input('What is the radius of the circle? '))
print(f'The area of the circle is : { 3.14 * (circle_r ** 2)} ')
#works as expected 
# Core is complete
print('Core challenges complete')

#Stretch Challenges attempt by Camden

# i'll import math every time eventhough i don't need to because 
# i know each little module can be used by it self if i need to comment something out later
# figured out the import math when i had to learn how to import things in lst weeks activty.
# The integrated Development enviorment provided by vscode or IDE makes pressiong tab ans scrolling easy to find things

#Stretch 1
print()
print()
print('stretch challenge 1: Math library import')
print()
print()
import math
s_circle_r =float(input('What is the radius of the circle? '))
print(f'The area of the circle is : { math.pi * (s_circle_r ** 2)} ')

#I noticed that running the python math libary is much more acrute.
#i imput 8 on both version and the anser was 200.96 the first way and it 
# was 201.06192...... the other way cool

#strech 2 
# 
# a3tempt 1
#slv = float(input('What value should be used for the length?'))
#s_square = slv **2
#s2_circle_r = math.pi *(slv ** 2)
#s_volume_cube = slv ** 3
#s_volume_sphere = (4/3) * math.pi * (slv ** 3)
#print(f'Area of a square: {s_square}')
#print(f'Area of a circle: {s2_circle_r}')
#print(f'Area of a cube: {s_volume_cube}')
#print(f'Area of a sphere: {s_volume_sphere}')

# attempt 2  more condensed 
print()
print()
print('stretch challenge 2: one vaule multiple answers')
print()
print()
import math
slv = float(input('What value should be used for the length?'))

print(f'Area of a square: {slv **2}')
print(f'Area of a circle: {math.pi *(slv ** 2)}')
print(f'Area of a cube: {slv ** 3}')
print(f'Area of a sphere: {(4/3) * math.pi * (slv ** 3)}')

#SAME RESULTS woot!

# Strecth 3
#cm to m conversion
#i want to so this all with one print function practice
print()
print()
print('stretch challenge 3 cm to m conversion')
print()
print()
import math
s3_square = float(input('What is the length of the side of the square in cm? '))
print(f'the area of a square is: {s3_square ** 2} cm^2 \nThe area in meters is: {(s3_square ** 2) / 10000} m^2.')
s3_rectangle_l = float(input('What is the length of the rectangle in cm? '))
s3_rectangle_w = float(input('what is the width of the rectangle in cm? '))
print(f'The area of the rectangle is: {s3_rectangle_l * s3_rectangle_w} cm^2 \nThe area in meters is: {(s3_rectangle_l * s3_rectangle_w) / 10000} m^2')
s3_radius = float(input('What is the radius of the circle in cm? '))
print(f'The area of the circle is: {math.pi * (s3_radius ** 2)} cm^2 \nThe area in meters is: {(math.pi * (s3_radius ** 2)) / 10000} m^2')


#EveryTHING works and now that I've compared to the sample solution I know I've done well

