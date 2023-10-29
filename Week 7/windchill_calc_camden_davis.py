#This code is writen by Camden Davis for CSE110 week 7 Windchill Calculator.



# Showing Creativity
#made sure teh reqyirements were met. Then i did the following.
# I made this loop to ask for temperature until the user was bored.
# I did not do much in the creativity. I made the program use the same unit the entire time instead of being reoatative and asking each time.
# I added time delay and I also addeda clear screen function made a while back ina few projects to mke the screen nice a ntidy during the loop.


# Requirements
# The following are the required components of this assignment:
# Write a function to calculate and return the wind chill based on a given temperature and wind speed.
# Write a function to convert from Celsius to Fahrenheit and return the converted temperature.
#   The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.
# Allow the user to enter the temperature in Celsius or Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit 
#   (using the conversion function created above) before using the formula above.
# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill (using the windchill function created above) 
#   for each of these wind speeds.
# Display the wind chill value to 2 decimals of precision.



import time
import os

def wind_chill(T, V):
    #these are the notes from the assignment for reference here.
    
    # Calculate and return the wind chill based on a given temperature and wind speed.
    # T is the temperature in degrees Fahrenheit
    # V is the wind speed in miles per hour
    # V^0.16 means V to the power of 0.16, which can be found in Python using the ** operator.
    return 35.74 + 0.6215 * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16

def celsius_to_fahrenheit(C):
    #Convert from Celsius to Fahrenheit and return the converted temperature.
    return (9 / 5) * C + 32

def clear_screen():  # Clear the Screen/terminal Function
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

unit = input('Enter the temperature unit (Celsius or Fahrenheit) Please enter "C" or "F":\n Please note the finale temperatures will all be displayed in Fahrenheit: ')
unit = unit.upper()

while True: #the main sauce of the program
    temperature = float(input(f"Enter the temperature in {unit}: "))

    if unit.upper() == 'C':
        # Convert Celsius to Fahrenheit before using the formula above.
        T = celsius_to_fahrenheit(temperature)
    elif unit.upper() == 'F':
        T = temperature
    else:
        print('That was not a valid answer. Only type "C" or "F":\n') # added \n to generate space for a prettier display.


    # Loop through wind speeds from 5 to 60 miles per hour, incrementing by 
    print("The Program will now display the Windchill at a each speed increment of 5mph from 5mph to 60mph.\n")
    time.sleep(3) #3second delay
    clear_screen() #clears the screen
    for V in range(5, 61, 5):
        # Calculate and display the wind chill (using the windchill function created above) for each of these wind speeds.
        
        print(f"At a temperature of {T:.2f} degrees Fahrenheit and a wind speed of {V} miles per hour, the wind chill is {wind_chill(T, V):.2f}.")
    # Ask if user wants to continue
    answer = input("Do you want try again and calculate at another temperature? (y/n): ")
    if answer.lower() != 'y':
        print("Thank you for using this program.")
        time.sleep(2)
        clear_screen()
        break
        