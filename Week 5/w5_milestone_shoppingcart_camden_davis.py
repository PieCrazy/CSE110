# This code is writen by Camden Davis for CSE110 week 5 Shopping Cart Milestone

# Milestone Requirements
# By the middle of the week, to help make sure you are on track to finish the assignment, 
# you need to complete the following:

# Have menu system that repeats until the user chooses quit.

# Create a list that will store the names of the items in the shopping cart.

# Complete the option to add the name of the item to the list.

# Complete the option to display the names of the items in the list.





names = []
prices = []

def add_item():
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    names.append(name)
    prices.append(price)
    print(f"{name} added to cart.")

def display_cart():
    if len(names) == 0:
        print("The cart is empty.")
    else:
        print("Contents of your shopping cart:")
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${prices[i]:>10.2f}")
        print(f"Total price: ${sum(prices):.2f}")

def remove_item():
    if len(names) == 0:
        print("The cart is empty.")
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

def compute_total(currency, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"The subtotal is {currency}{subtotal:.2f}.")
    print(f"The tax is {currency}{tax:.2f}.")
    print(f"The total price of the cart is {currency}{total:.2f}.")

def menu():
    while True:
        print("Menu:")
        print("1. Add a new item")
        print("2. Display the contents of the shopping cart")
        print("3. Remove an item")
        print("4. Compute the total")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            display_cart()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            compute_total(currency, tax_rate)
        
        elif choice == "5":
            quit()

        else:
            break

currency = input("What currency will be used for the shopping cart? (for example $, €,): ")
tax_rate = float(input("Enter your tax rate as a decimal. (for example 0.07  for 7%): "))

menu()