# This code is writen by Camden Davis for CSE110 week 2 project Meal Price Calculator 

# PLEASE NOTE
# I made a change to two questions after emailing Brother Gold. He gave mer permision to do so.
# I left a note at that part of the code to read please don't skip that while overviewing the code.


# SHOWING CREATIVITY AND EXCEEDING REQUIREMENTS
# 
# I added functions in general (I remembered how to do that or the basicas from c++ class i took)
# SHOWING CREDIT FOR LEARNING MORE ON PYTHON TO MAKE THE EXCEEDING THINGS TO WORK 
# I looked these up for these up for the last project but i'll be re using them here for this one too
# so i've included the links again for this knowlegde i gained last time.
#
#  i had to look up the clear function for python from stack overflow and i implemented it here
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
# comment from opticalMagician had the clear screen effect i ustlized for this
#
# I also wanted a time delay for the Generating portion and intro so they didn all appear at once 
# I learned how the time delay worked
# by reading on about the sleep function on this website
# https://realpython.com/python-sleep/
# 
# I also wanted to add a "Yes or no"/ true false typeQuestion with the chance to enter it more than once incase the 
# user didn't anser acceptablevaule aka not yes or no for another story time or exit comepletly.
#  i found the yes no code from https://codeigo.com/python/yes-or-no-question/ it had a nice 3 step tutorial
#  with that being said that was for if else statements. i also needed to have the program restart.
# https://stackoverflow.com/questions/11459102/how-do-i-re-run-code-in-python This comment by peter cokcrom
#
#
# I looked these up specifiaclly for this project
#https://stackoverflow.com/questions/11489326/print-a-float-with-precision-right-justified
# i however never implemented the way it talked about as i had trouble getting that way to work



# WHAT THE PROGRAM DOES.

# I have the main code run within my MAIN program which i define right here
#   main
# the program will genrate the price of a meal based on several factors it asks for and you imput.
# the program will then generate a nice looking recipt for you
# main also clalls the function clear a few times to clear the screen to make it nice and pretty.
#
# I Then made the restart portion a seperate function that gets called at the end of main,
# the restart function has the while loop runnning and checks for specfic answers on whether or not to restart
# if no valid anser is entered it gives you valid ansers you can type and then prompts you again until you type a valid answer
# if yes it calls main again and the program resarts. If no it will clear and exit

def main():
    
    #intro to program with delay for "animation" effect

    print()
    print()
    print('Welcome to Meal Price Calculator. ')
    print()
    print()
    # time delay
    import time
    time.sleep(3) # Sleep for 3 seconds
    
    #Clearing the title
    import os
    def clear():
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
    clear()
    #Cleared the title
    
    #Gathering the information
    #Changing the core a little bit for clarity (not asking number of people but rather number of eahc type of meal)
    print('In order to help you best, please enter the following information:')
    print() #creating formating space
    currency = input('What currency is being used? (for example $, €, etc.) ')
    print(f'Thank you. All prices will now be calculated using {currency}.')
    print()
     # time delay
    import time
    time.sleep(3) # delay for 3 seconds kinda animation
    import os
    def clear():
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
    clear()
    print('Please enter the information even if you do not want to get an item. \n Please only input the numbers.\n For Example Price: 2.40')
    print()
    meal_child = float(input("What is the price of a child's meal? ")) #using "blah " because of the ' in child's
    meal_adult = float(input("What is the price of an adult's meal? "))
    
    # ATTENTION to the grader
    # Before I get deducted points here, emailed and asked Brother Gold if could change the question to quantity 
    # of meals instead of quantity of people. He replied that was acceptable. so instead of asking 
    # How many children are there i'm asking how many childrens meals do you want, and the same with adults. I'm asking
    # How many adult meals do you want instead of how many adults are there. This makes more sense based on it 
    # being a meal calucatlator and people share meals all the time. It accomplishes the same goal but makes more sense
    # in the way I implemented the question. 
    # Thank you,
    # - Camden
    
    
    num_child_meal = int(input('How many children meals do you want to order? '))
    num_adult_meal = int(input('How many adult meals do you want to order? '))
    s_tax = float(input('What is the sales tax rate? (for example "3" meaning 3%) '))
    print()
    print('Calculating your meal total')
    time
    time.sleep(2) # Sleep for 2 seconds for dramaticd effect. use to b5 but that delay was too long
    
   #The orginal way i decided to do it and it works good enough
   
    # subtotal = (num_adult_meal * meal_adult ) + (num_child_meal * meal_child)
    # print(f'Subtotal: {currency}{subtotal:.2f}')
    # s_tax_total = subtotal * (s_tax / 100)
    # print(f'Sales tax: {currency}{s_tax_total:.2f}')
    # total = subtotal + s_tax_total
    # print(f'Total: {currency}{total:.2f}')
    # payment_amount = float(input('What is the payment amount? '))
    # change = payment_amount - total
    # print(f'Change: {currency}{change:.2f}')
    # meal_price_adult_subtotal = (num_adult_meal * meal_adult)
    # meal_price_child_subtotal = (num_child_meal * meal_child)
    # print('Reciept')
    # print()
    # print(f"Children's meals: {num_child_meal} @ {currency}{meal_child:.2f} \n                     {currency}{meal_price_child_subtotal:.2f} ")
    # print(f"Adult meals: {num_adult_meal} @ {currency}{meal_adult:.2f} \n                {currency}{meal_price_adult_subtotal:.2f} ")

    # print(f'Subtotal: {currency}{subtotal:.2f}')
    # print(f'Sales tax: {currency}{s_tax_total:.2f}')
    # print(f'Total: {currency}{total:.2f}')
    # print(f'Payment total: {currency}{payment_amount:.2f}')
    # print(f'Change due: {currency}{change:.2f}')
    
    
    #New way that aligns it right mostly (spent a long time to get to this point)
    subtotal = (num_adult_meal * meal_adult ) + (num_child_meal * meal_child)
    print(f'Subtotal: {currency}{subtotal:.2f}')
    s_tax_total = subtotal * (s_tax / 100)
    print(f'Sales tax: {currency}{s_tax_total:.2f}')
    total = subtotal + s_tax_total
    print(f'Total: {currency}{total:.2f}')
    payment_amount = float(input('What is the payment amount? '))
    change = payment_amount - total
    print(f'Change: {currency}{change:.2f}')
    meal_price_adult_subtotal = (num_adult_meal * meal_adult)
    meal_price_child_subtotal = (num_child_meal * meal_child)
    import time
    time.sleep(3) #adding a delay here because otherwise its a fast an unexpected reciept
    print()
    print()
    print()
    print('Here is your Reciept')
    print()
    print()
    print()
    #attempting to line everyhting up before thew align right funtion
    print('You ordered')
    print()
    print(f"Children's meals: {num_child_meal:>20} @ {currency}{meal_child:.2f} \n                      {currency:>20}{meal_price_child_subtotal:.2f} ")
    print(f"Adult meals:      {num_adult_meal:>20} @ {currency}{meal_adult:.2f} \n                      {currency:>20}{meal_price_adult_subtotal:.2f}")
    print()
    print(f'Subtotal:             {currency:>20}{subtotal:.2f}')
    print(f'Sales tax:            {currency:>20}{s_tax_total:.2f}')
    print()
    print(f'Total:                {currency:>20}{total:.2f}')
    print(f'Payment total:        {currency:>20}{payment_amount:.2f}')
    print()
    print(f'Change due:           {currency:>20}{change:.2f}')
    print()
    print()
    import time
    time.sleep(3) #pauses for 3 seconds before displaying the restart code.

    #This Function will Restart the program if that is the desired result.
    #It also clears the screen to make things nice and tidy
    #it also checks the users input to verify that the answer is an acceptble form of yes or no
    #based on the question and restarts on if the aceptable anser is provided.
    def restart():
    
        while True:
            restart_tf =  'Would you like another meal to be calculated?'  
            restart_tf_a = input(f'{restart_tf} (yes or no): ')
            restart_tf_a = restart_tf_a.strip().lower()
            if restart_tf_a in ['yes', 'y' , 'ya']:
                print('One Moment Please')   
                import time
                time.sleep(2)
                import os
                def clear():
                    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
                clear()
                main()
            elif restart_tf_a in ['no', 'n' , 'na']:
                import os
                def clear():
                    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
                clear()
                
                print()
                print()
                print()
                print('Thank you for using the Meal Price Calculator. Goodbye.')
                print()
                print()
                print()
                
                import time
                time.sleep(3)
                clear()
                exit()
                   
            else: 
                print(f'You may only input yes/y/ya or no/n/na. You anserwed {restart_tf_a} \nThat is not a valid answer. Please try again.' )
                print()
    restart()
main()