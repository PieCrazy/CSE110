# This code is writen by Camden Davis for CSE110 week 5 Shopping Cart.
# This is 
# I've listed the reqirements below.
#   GOING ABOVE AN BEYOND THINGS I'VE DONE
#
# 
# https://www.w3schools.com/python/ref_func_zip.asp  I learned what his function was so i could basically marry the item and the price together.
# 
# 
"""
##                                      Project Description
# For this project you will create a program that stores a list of products in a shopping cart along with their prices.
# The user should have the ability to add items to the list, remove them, and see the total price of the cart.
#
# For the milestone deliverable, you only need to worry about storing a list of the names of the items
# (not the prices yet), and only need to be able to add new items and display the list. Then, for the complete project,
# you'll add the ability to store the prices, remove items, and compute the total.
# 
##                                          Assignment
# For this project, the user will be given a menu and have the ability to choose items from the menu.
# The options in the menu include the following:
#
#   Add a new item
#       The program asks the user for the name of the item. For the final project deliverable it 
#       should also ask the user for the price of the item.
#       The program stores these values in a list. When you are working on the milestone deliverable, 
#       you will only need one list (to store the names). For the final project, when you are storing both 
#       names and prices,
#       you should use two lists, one for the names and one for the prices.
#
#   Display the contents of the shopping cart
#       The program should display all of the items in the shopping cart, one per line. 
#       For the milestone deliverable, you only need to display the names of the items. 
#       For the final project deliverable, the price of each item should be displayed next to the item.
#       Also, for the final project, the program should also display the number associated with each item in the list,
#       beginning with 1. This is different than how Python will store them, because it will start counting at 0,
#       but to make it more natural for the user, you should start the numbers at 1.
#
#   Remove an item (only needed for the final project deliverable)
#       The user types in the number of the item they want to remove and the item is removed from the list.
#       In order to do this correctly, your program will need to do each of the following:
#       Convert the number the user enters to a 0-based index. For example, 
#       if they want to remove the second item in the list they will type "2" 
#       (because they will see the numbers starting at 1), but this item will be stored in Python at index 1 
#       (because Python will start counting at 0).
#       Make sure that the index is within the bounds of the current list (for example,
#       you cannot remove item 10 if there are only 5 items in the list). If the index is outside the bounds of 
#       the list, you should not attempt to remove it, but rather, display a message informing the user that they 
#       have made an invalid choice.
#       Remove the item at that spot in the list. Don't forget that if you are storing names and prices, 
#       you'll need to remove both the name and the price from their respective lists.
#   Compute the total (only needed for the final project deliverable)
#       The program should iterate through each item in the list and add up the prices and then display
#       the total amount to the user.
#
#   Quit
#
##
##                                          Milestone Requirements
# By the middle of the week, to help make sure you are on track to finish the assignment, 
# you need to complete the following:
#
# Have menu system that repeats until the user chooses quit.
#
# Create a list that will store the names of the items in the shopping cart.
#
# Complete the option to add the name of the item to the list.
#
# Complete the option to display the names of the items in the list.
#
##                                         Final Requirements
# In addition to the functionality above, for the final project, you also need to complete the following:
#
# Store prices as well as names.
#
# Change the add functionality to also ask for and store the price of the item.
#
# Change the display functionality to also display the prices of the items.
#
# When displaying the items, display a number in front of each item. The numbers should start with 1.
#
# Complete the option to display the total amount of the prices of all the items in the shopping cart.
#
# Whenever prices are displayed, they should be shown to two decimal places and include the 
# appropriate currency symbol (for example $, €, etc.)
#
# Complete the option to remove an item from the shopping cart.
#
# When removing an item, you should verify the following:
#
# Both the item name and price are removed from their respective lists.
#
# The number the user enters should be converted to a 0-based index and checked to make sure it is
# within the bounds of the list.
#
# The program allows you to remove any item from the list including the first one and the last one.
# (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)
#






I tried many differnt things. i just commented out things and tried again again until i got a working way i liked.








# #global things for the program

# import time
# import os
#     #declaring some global variables and lists (setting )
# currency = ""
# s_tax = 0  #setting zeros to start
# names = []
# prices = []
# running_total = 0  #setting zeros to start
# subtotal = 0

# def main(): #This is the basic logic.
#     title()
#     intro()
#     shopping_cart()
      
    
# def title(): # title screen
#     print()
#     print()
#     print("Welcome to Cam's generic Shopping Cart program. ")
#     print()
#     print()
#     time.sleep(3) # Sleep for 3 seconds
#     clear_screen() #clear title    
    
# def intro():# introduction and #Gathering the information 
    
#     #Changing the core a little bit for clarity (not asking number of people but rather number of eahc type of meal)
#     print('In order to help you best, please enter the following information:')
#     print() #creating formating space
#     currency = input('What currency will be used for the shopping cart? (for example $, €,) \nPlease type (USD or EUR):')
#     print(f'Thank you. All prices will now be calculated using {currency}.')
#     print()
#     time.sleep(2) # delay for 2 seconds kinda animation
#     s_tax = float(input('What is the sales tax rate? (for example "3" meaning 3%) '))
#      # time delay
#     time.sleep(2) # delay for 2 seconds kinda animation
#     clear_screen()
    
# def shopping_cart(): #main program here  after each time someone does something it needs to come back to this one
#     print('Please select one of the following: (Number only)')
#     print('1. Add Item')
#     print('2. Remove Item')
#     print('3. View Cart')
#     print('4. Compute Total')
#     print('5. Quit')
#     print('6. Restart')
#     select_sc = input().strip().lower()
#     select_sc_ans = 'no_answer'
# # i could do something like this 
# # # while True:
#     # print("\nMenu:")
#     # print("1. Add a new item")
#     # print("2. Display the contents of the shopping cart")
#     # print("3. Remove an item")
#     # print("4. Quit")
    
#     # choice = input("Enter your choice: ")
    
#     # if choice == "1":
#     #     add_item(names, prices)
#     # elif choice == "2":
#     #     display_items(names, prices)
#     # elif choice == "3":
#     #     remove_item(names, prices)
#     # elif choice == "4":
#     #     break
#     # else:
#     #     print("Invalid choice.")

# # i do this like this so that no errors can creep in and break the program.  
# # its alot more code to do it this way though. and thats okay
#     while (select_sc_ans == 'no_answer'):
#         if (select_sc == '1'):
#             select_sc_ans = 'answered'
#             clear_screen()
#             add_item(names, prices)
#         elif(select_sc == '2'):
#             select_sc_ans = 'answered'
#             clear_screen()
#             remove_item(names, prices)
#         elif(select_sc == '3'):
#             select_sc_ans = 'answered'
#             clear_screen()
#             view_cart(
                
#             )
#         elif(select_sc == '4'):
#             select_sc_ans = 'answered'
#             clear_screen()
#             compute_total()
#         elif(select_sc == '5'):
#             select_sc_ans = 'answered'
#             clear_screen()
#             quit_the_program()
#         elif(select_sc == '6'):
#             select_sc_ans = 'answered'
#             clear_screen()
#             restart_program()
#         else:
#             print("That is not an acceptable answer! # only please.")
#             print('Please Type one of the following answers:')
#             print('1. Add Item')
#             print('2. Remove Item')
#             print('3. View Cart')
#             print('4. Compute Total')
#             print('5. Quit')
#             print('6. Restart')
#             select_sc = input().strip().lower()       
#     print('Okay, returning to Main Menu.')
#     shopping_cart()
    
# def view_cart():
#     print('The contents of the shopping cart are: ')
# # LIST ALL THE CRAP like this
# # 1. item name     -    $3.45
# # 2. intem blah  -      $2.50




# def view_cart(names, prices, currency):
#     print("Shopping Cart:")
#     sorted_items = sorted(zip(prices, names))
#     for i, item in enumerate(sorted_items):
#         price_str = f"{item[0]:.2f}"
#         if currency == "USD":
#             price_str = "$" + price_str
#         elif currency == "EUR":
#             price_str = "€" + price_str
#         print(f"{i+1}. {item[1]:<20} {price_str:>10}")
#     print()
#     shopping_cart()
    
# def add_item(names, prices):
#     name = input("Enter the name of the item: ")
#     price = float(input("Enter the price of the item: "))
#     names.append(name)
#     prices.append(price)
    
# def remove_item():
#     print('Which item would you like to remove? ')  # say like 4  and it removes item 4
#     #  view_cart()  list all items here so they know what to remove   
#     print('Item Removed. ')
    
#     print('Okay, returning to Main Menu.')
#     shopping_cart()
    
# def remove_item(names, prices):
#     index = int(input("Enter the number of the item you want to remove: ")) - 1
#     if index < 0 or index >= len(names):
#         print("Invalid index.")
#         return
#     names.pop(index)
#     prices.pop(index)
    
# def compute_total():
#     print()
#     #print(f'The total price of the items in the shopping cart is {currency}{totalprice.}')
#     print('Do you want a breakdown of the shopping cart? ')
#     compute_total_sc = input().strip().lower()
#     compute_total_sc_ans = 'no_answer'
#     while (compute_total_sc_ans == 'no_answer'):
#         if (compute_total_sc == 'yes'):
#             print('Generating breakdown of the cart.')
#             time.sleep(2)
#             clear_screen()
#             running_total = 0
#             for subtotal in cart_items_price:
#                 running_total += subtotal
#             print(f'The subtotal is: {running_total:.2f}')
            
            
# def compute_total(prices, currency):
#     subtotal = sum(prices)
#     tax = float(input('What is the tax rate? For for example 3% type 3')) 
#     tax = subtotal * (tax / 100)
#     total = subtotal + tax
#     print(f"Subtotal: {currency} {subtotal:.2f}")
#     print(f"Tax: {currency} {tax:.2f}")
#     print(f"Total: {currency} {total:.2f}")
     
#     time
#     time.sleep(2) # Sleep for 2 seconds for dramaticd effec
    
# def quit_the_program():
#     print('are you sure if statements')
#     quit_sc = input().strip().lower()
#     quit_sc_ans = 'no_answer'
#     while (quit_sc_ans == 'no_answer'):
#         if (quit_sc == '1'):
#             quit_sc_ans = 'answered'
#             clear_screen()
#             add_item()# similar to the restart program but it will do are you sure or go back to where you where
#             print('Thank you for using the Shopping Cart Program. Goodbye.')
#             time.sleep(3)
#             clear_screen()
#             exit()
#         elif(quit_sc == '2'):
#             print('Returning to menu. ')
#             time.sleep(2)
#             quit_sc_ans = 'answered'
#             clear_screen()
#             shopping_cart()
#         else:
#             print("That is not an acceptable answer! # only please.")
#             print('1. Yes I want to quit.')
#             print('2. No I do not want to quit')
#             quit_sc = input().strip().lower()  
            
# def clear_screen():  # Clear the Screen/terminal Function
#         os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
        
# def restart_program():   #restarts the shopping cart experience.
#             while True:
#                 restart_tf =  'Would you like to make another cart?'  
#                 restart_tf_a = input(f'{restart_tf} (yes or no): ')
#                 restart_tf_a = restart_tf_a.strip().lower()
#                 if restart_tf_a in ['yes', 'y']:
#                     print()
#                     print('One moment to restart')   
#                     time.sleep(2)
#                     clear_screen()
#                     intro()
#                 elif restart_tf_a in ['no', 'n']:
#                     clear_screen()
#                     print()
#                     print('Thank you for using the Shopping Cart Program. Goodbye.')
#                     time.sleep(3)
#                     clear_screen()
#                     exit()
#                 else: 
#                     print(f'You may only input yes or no. You anserwed {restart_tf_a} \n That is not a valid answer. Please try again.' )              

# if __name__ == '__main__':
#      main()
     
     
     
     
     



"""

import time
import os


names = []
prices = []
currency = ""

def main(): #This is the basic logic.
     title()
     intro()
     menu()

def title(): # title screen
     print()
     print()
     print("Welcome to Cam's generic Shopping Cart program. ")
     print()
     print()
     time.sleep(3) # Sleep for 3 seconds
     clear_screen() #clear title  

def intro():# introduction and #Gathering the information 
    
     #Changing the core a little bit for clarity (not asking number of people but rather number of eahc type of meal)
     print('In order to help you best, please enter the following information:')
     print() #creating formating space
     currency = input("What currency will be used for the shopping cart? (for example $, €,): ")
     print(f'Thank you. All prices will now be calculated using {currency}.')
     print()
     global tax_rate
     tax_rate = float(input("Enter your tax rate as a decimal. (for example 0.07  for 7%): "))
     
      # time delay
     time.sleep(2) # delay for 2 seconds kinda animation
     clear_screen()


def add_item():
    item = input("Enter the name of the item: ")
    price = float(input('Enter the price of the item (do not inlcude $. Only the numbers like "2.65"): '))
    names.append(item)
    prices.append(price)
    print(f"{item} added to cart.")

def display_cart():
    if len(names) == 0:
        print("Can't display anything. The cart is empty.")
    else:
        print("Contents of your shopping cart:")
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${prices[i]:>10.2f}")
        print(f"Subtotal price: ${sum(prices):.2f}")

def remove_item():
    if len(names) == 0:
        print("Can't remove anything. The cart is empty.")
    else:
        print("Items in your shopping cart:")
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${prices[i]:.2f}")
        index = int(input("Enter the number of the item you want to remove: ")) - 1
        if index < 0 or index >= len(names):
            print("Invalid choice.")
        else:
            names.pop(index)
            prices.pop(index)
            print(f"Item {index+1} removed from cart.")
            display_cart()



def compute_total():
     subtotal = sum(prices)
     subtotal = float(subtotal)
     tax = subtotal * tax_rate
     total = subtotal + tax
     print(f"The subtotal is {currency}{subtotal:.2f}.")
     print(f"The tax is {currency}{tax:.2f}.")
     print(f"The total price of the cart is {currency}{total:.2f}.")
    



def clear_screen():  # Clear the Screen/terminal Function
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
        
def restart_program():   #restarts the shopping cart experience but doesn't call the title. thats why thers the break loop.
            while True:
                restart_tf =  'Would you like to make another cart?'  
                restart_tf_a = input(f'{restart_tf} (yes or no): ')
                restart_tf_a = restart_tf_a.strip().lower()
                if restart_tf_a in ['yes', 'y']:
                    print()
                    print('One moment to restart')   
                    time.sleep(2)
                    clear_screen()
                    intro()
                    break
                elif restart_tf_a in ['no', 'n']:
                    clear_screen()
                    print()
                    print('Thank you for using the Shopping Cart Program. Goodbye.')
                    time.sleep(3)
                    clear_screen()
                    exit()
                else: 
                    print(f'You may only input yes or no. You anserwed {restart_tf_a} \n That is not a valid answer. Please try again.' )              


def menu():
    while True:
        print("Menu:")
        print("1. Add a new item")
        print("2. Display the contents of the shopping cart")
        print("3. Remove an item")
        print("4. Compute the total")
        print("5. Restart")
        print("6. Quit")

        choice = input("Enter your choice: ")
        choice = choice.strip().lower()
        # orginal way i did it. 
        #  if choice == "1":
        #     add_item()

        # elif choice == "2":
        #     display_cart()

        # elif choice == "3":
        #     remove_item()

        # elif choice == "4":
        #     compute_total(currency, tax_rate)
        
        # elif choice == "5":
        #     quit()
        
        
        if choice in ["1", 'add']:
            clear_screen()
            add_item()
            

        elif choice in ["2","show","display"]:
            clear_screen()
            display_cart()
            

        elif choice in ["3","remove"]:
            clear_screen()
            remove_item()
            

        elif choice in ["4","compute"]:
             clear_screen()
             compute_total()
            
        
        elif choice in ["5", "restart"]:
            clear_screen()
            restart_program()
            
        elif choice in ["6", "quit "]:
            clear_screen()
            exit()
            

        else:
            print(f'You may only input a whole number like "1" you entered {choice}.\n That is not a valid answer.')
                  
if __name__ == '__main__':
      main()