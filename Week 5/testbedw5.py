# # # def add_item(names, prices):
# # #     name = input("Enter the name of the item: ")
# # #     price = float(input("Enter the price of the item: "))
# # #     names.append(name)
# # #     prices.append(price)

# # # def display_items(names, prices):
# # #     print("Shopping Cart:")
# # #     for i in range(len(names)):
# # #         print(f"{i+1}. {names[i]} - ${prices[i]:.2f}")
# # #     print(f"Total price: ${sum(prices):.2f}")
    
    
# # # def display_items(names, prices):
# # #     print("Shopping Cart:")
# # #     sorted_items = sorted(zip(prices, names))
# # #     for i, item in enumerate(sorted_items):
# # #         print(f"{i+1}. {item[1]} - ${item[0]:.2f}")
# # #     print(f"Total price: ${sum(prices):.2f}")




# # # def remove_item(names, prices):
# # #     index = int(input("Enter the number of the item you want to remove: ")) - 1
# # #     if index < 0 or index >= len(names):
# # #         print("Invalid index.")
# # #         return
# # #     names.pop(index)
# # #     prices.pop(index)

# # # names = []
# # # prices = []

# # # while True:
# # #     print("\nMenu:")
# # #     print("1. Add a new item")
# # #     print("2. Display the contents of the shopping cart")
# # #     print("3. Remove an item")
# # #     print("4. Quit")
    
# # #     choice = input("Enter your choice: ")
    
# # #     if choice == "1":
# # #         add_item(names, prices)
# # #     elif choice == "2":
# # #         display_items(names, prices)
# # #     elif choice == "3":
# # #         remove_item(names, prices)
# # #     elif choice == "4":
# # #         break
# # #     else:
# # #         print("Invalid choice.")
        
        
        
 
 
 
 
 
 
 
 
        
        
# # # def add_item(names, prices):
# # #     name = input("Enter the name of the item: ")
# # #     price = float(input("Enter the price of the item: "))
# # #     names.append(name)
# # #     prices.append(price)

# # # def display_items(names, prices):
# # #     print("Shopping Cart:")
# # #     sorted_items = sorted(zip(prices, names))
# # #     subtotal = sum(prices)
# # #     tax = subtotal * 0.07
# # #     total = subtotal + tax
# # #     for i, item in enumerate(sorted_items):
# # #         print(f"{i+1}. {item[1]} - ${item[0]:.2f}")
# # #     print(f"Subtotal: ${subtotal:.2f}")
# # #     print(f"Tax: ${tax:.2f}")
# # #     print(f"Total: ${total:.2f}")

# # # def remove_item(names, prices):
# # #     index = int(input("Enter the number of the item you want to remove: ")) - 1
# # #     if index < 0 or index >= len(names):
# # #         print("Invalid index.")
# # #         return
# # #     names.pop(index)
# # #     prices.pop(index)

# # # names = []
# # # prices = []

# # # while True:
# # #     print("\nMenu:")
# # #     print("1. Add a new item")
# # #     print("2. Display the contents of the shopping cart")
# # #     print("3. Remove an item")
# # #     print("4. Quit")
    
# # #     choice = input("Enter your choice: ")
    
# # #     if choice == "1":
# # #         add_item(names, prices)
# # #     elif choice == "2":
# # #         display_items(names, prices)
# # #     elif choice == "3":
# # #         remove_item(names, prices)
# # #     elif choice == "4":
# # #         break
# # #     else:
# # #         print("Invalid choice.")
        
        
        
        
        
        


# # def add_item(names, prices):
# #     name = input("Enter the name of the item: ")
# #     price = float(input("Enter the price of the item: "))
# #     names.append(name)
# #     prices.append(price)


# # def display_items(names, prices, currency):
# #     print("Shopping Cart:")
# #     sorted_items = sorted(zip(prices, names))
# #     subtotal = sum(prices)
# #     tax = subtotal * 0.07
# #     total = subtotal + tax
# #     for i, item in enumerate(sorted_items):
# #         price_str = f"{item[0]:.2f}"
# #         if currency == "USD":
# #             price_str = "$" + price_str
# #         elif currency == "EUR":
# #             price_str = "€" + price_str
# #         print(f"{i+1}. {item[1]:<20} {price_str:>10}")
# #     print(f"Subtotal: {currency} {subtotal:.2f}")
# #     print(f"Tax: {currency} {tax:.2f}")
# #     print(f"Total: {currency} {total:.2f}")

# # def remove_item(names, prices):
# #     index = int(input("Enter the number of the item you want to remove: ")) - 1
# #     if index < 0 or index >= len(names):
# #         print("Invalid index.")
# #         return
# #     names.pop(index)
# #     prices.pop(index)

# # names = []
# # prices = []

# # currency = input("Enter your preferred currency (USD or EUR): ")

# # while True:
# #     print("\nMenu:")
# #     print("1. Add a new item")
# #     print("2. Display the contents of the shopping cart")
# #     print("3. Remove an item")
# #     print("4. Quit")
    
# #     choice = input("Enter your choice: ")
    
# #     if choice == "1":
# #         add_item(names, prices)
# #     elif choice == "2":
# #         display_items(names, prices, currency)
# #     elif choice == "3":
# #         remove_item(names, prices)
# #     elif choice == "4":
# #         break
# #     else:
# #         print("Invalid choice.")


# def add_item(names, prices):
#     name = input("Enter the name of the item: ")
#     price = float(input("Enter the price of the item: "))
#     names.append(name)
#     prices.append(price)

# def display_items(names, prices, currency):
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

# # def compute_total(prices, currency, tax_rate):
# #     subtotal = sum(prices)
# #     tax = subtotal * tax_rate
# #     total = subtotal + tax
# #     print(f"Subtotal: {currency} {subtotal:.2f}")
# #     print(f"Tax: {currency} {tax:.2f}")
# #     print(f"Total: {currency} {total:.2f}")
# def compute_total():
#     display_items()
#     sub_total = sum([item[1] * item[2] for item in items])
#     tax = sub_total * 0.07
#     total = sub_total + tax
#     print(f"{'Sub-Total:':<15} ${sub_total:>7.2f}")
#     print(f"{'Tax:':<15} ${tax:>7.2f}")
#     print(f"{'Total:':<15} ${total:>7.2f}")

# def remove_item(names, prices):
#     index = int(input("Enter the number of the item you want to remove: ")) - 1
#     if index < 0 or index >= len(names):
#         print("Invalid index.")
#         return
#     names.pop(index)
#     prices.pop(index)

# def main_menu():
#     names = []
#     prices = []

#     currency = input("Enter your preferred currency (USD or EUR): ")
#     tax_rate = float(input("Enter the tax rate (e.g. 0.07 for 7%): "))

#     while True:
#         print("\nMenu:")
#         print("1. Add a new item")
#         print("2. Remove an item")
#         print("3. View shopping cart")
#         print("4. Compute total")
#         print("5. Quit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_item(names, prices)
#         elif choice == "2":
#             remove_item(names, prices)
#         elif choice == "3":
#             display_items(names, prices, currency)
#         elif choice == "4":
#             compute_total(prices, currency, tax_rate)
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice.")

# main_menu()






# names = []
# prices = []

# def add_item():
#     name = input("Enter the name of the item: ")
#     price = float(input("Enter the price of the item: "))
#     names.append(name)
#     prices.append(price)
#     print(f"{name} added to cart.")

# def display_cart():
#     if len(names) == 0:
#         print("The cart is empty.")
#     else:
#         print("Contents of your shopping cart:")
#         for i in range(len(names)):
#             print(f"{i+1}. {names[i]} - ${prices[i]:>10.2f}")
#         print(f"before taxs you cart price is: ${sum(prices):.2f}")

# # def remove_item():
# #     if len(names) == 0:
# #         print("The cart is empty.")
# #     else:
# #         index = int(input("Enter the number of the item you want to remove: ")) - 1
# #         if index < 0 or index >= len(names):
# #             print("Invalid choice.")
# #         else:
# #             names.pop(index)
# #             prices.pop(index)
# #             print(f"Item {index+1} removed from cart.")
# def remove_item():
#     if len(names) == 0:
#         print("The cart is empty.")
#     else:
#         print("Items in your shopping cart:")
#         for i in range(len(names)):
#             print(f"{i+1}. {names[i]} - ${prices[i]:.2f}")
#         index = int(input("Enter the number of the item you want to remove: ")) - 1
#         if index < 0 or index >= len(names):
#             print("Invalid choice.")
#         else:
#             names.pop(index)
#             prices.pop(index)
#             print(f"Item {index+1} removed from cart.")

# def compute_total(currency, tax_rate):
#     subtotal = sum(prices)
#     tax = subtotal * tax_rate
#     total = subtotal + tax
#     print("Contents of your shopping cart:")
#     for i in range(len(names)):
#         print(f"{names[i]} - ${prices[i]:>10.2f}")
#     print(f"Subtotal: ${subtotal:.2f}")
#     print(f"Tax: ${tax:.2f}")
#     print(f"Total price: ${total:.2f}")

# def menu():
#     while True:
#         print("Menu:")
#         print("1. Add a new item")
#         print("2. Display the contents of the shopping cart")
#         print("3. Remove an item")
#         print("4. Compute the total")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_item()

#         elif choice == "2":
#             display_cart()

#         elif choice == "3":
#             remove_item()

#         elif choice == "4":
#             compute_total(currency, tax_rate)

#         else:
#             break

# currency = input("Enter your currency symbol: ")
# tax_rate = float(input("Enter your tax rate as a decimal: "))

# menu()




#this works best

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

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            display_cart()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            compute_total(currency, tax_rate)

        else:
            break

currency = input("What currency will be used for the shopping cart? (for example $, €,): ")
tax_rate = float(input("Enter your tax rate as a decimal. (for example 0.07  for 7%): "))

menu()
