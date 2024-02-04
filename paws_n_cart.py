"""
***************************** PAWS'N'CART *****************************

This program creates a shopping cart, 
which allows the user to add available items, to remove items, 
to calculate the total cost and to checkout. 
The focus for this project is user friendliness.

*** Program has been improved using functions ***

"""

#~~~~~~~~ Creating Functions ~~~~~~~~

# Function to display a separator for better readability
def separator(length = 95, symbol = "-"):
    print(length * symbol)


# Function to display cart:
def cart_display():
    count = 0
    print("This is your shopping cart:\n")
    for item, price in zip(items, prices):
        count += 1
        quant_index = items.index(item)
        shopping_cart = f"{count}. £{price} \t\t {item:40} " \
                        f"\t\t Quantity: {quant[quant_index]}"

        print(shopping_cart)


# Function to display stock list and 
# their price from which the user can choose.
def item_menu():
    counter = 0
    print("\nList of items available:\n")
    for price, item in zip(stock_price, stock):
                    counter += 1
                    print(f"{counter}. £{price}\t\t\t{item}")


# Function to add item:
def add_item():
    items.append(stock[selection])
    items_index = items.index(stock[selection])
    prices.append(stock_price[selection])
    quant[items_index] += 1


# Function to remove item:
def remove_item():
    items.remove(items[removed_item])
    prices.remove(prices[removed_item])
    quant.pop(removed_item)


# Function to return the length of items[]:
def length_items():
    length = len(items)
    separator()
    print(f"Invalid option. Please select 1-{length}.\n")



items = []
prices = []
quant = [0, 0, 0]
cart_total = 0
stock = ["Pedigree Wet Adult Dog Food (36 pouches)",
         "Whiskas Dry Cat Food (950g)", "Tetra Goldfish Mix (27L)"]
stock_price = [13.50, 10.30, 45.49]



# Main code
print("\n***** Welcome to Paws n Cart! *****\n")


done = False
while not done:
    separator()


    # Display the cart of items with their prices and the quantity
    if items:
        cart_display()
    else:
        print("Your shopping cart is empty.")


    separator()
    # Display the main menu
    choice = input("\nMain Menu:\n\n"
                   "1. Add an item to your cart\n"
                   "2. Remove an item from your cart\n"
                   "3. View the total cost of your cart\n"
                   "4. Checkout\n" 
                   "\nPlease enter the number of the option "
                   "you would like to choose (1-4):\n")


    separator()
    if choice == "1":
        # Display stock and price the user can choose from.
        while True:
            item_menu()

            selection = input("\nWhat item would you like "
                              "to add to your cart (1-3)?\n"
                              "To return to the main menu, "
                              "please enter zero (0):\n")


            try:

                # Give the option to return to main menu,
                # in case above selection was by mistake.
                if selection == "0":
                    break

                # Correct indexing
                selection = int(selection) - 1

                # Check if item already in cart:
                # If it is, increase quantity and if not,
                # add item and price to cart.
                if stock[selection] in items:
                    items_index = items.index(stock[selection])
                    quant[items_index] += 1
                    cart_total += stock_price[selection]
                    print(f"\n{stock[selection]} has been added "
                          f"to your cart successfully.")
                    break

                else:
                    add_item()
                    cart_total += stock_price[selection]
                    print(f"\n{stock[selection]} has been added "
                          f"to your cart successfully.")
                    break

            except IndexError:
                separator()
                print("Invalid option. Please select 1-3.\n")
            except ValueError:
                separator()
                print("Invalid option. Please select 1-3.\n")
            except Exception as e:
                print("An unexpected error occurred:", e)


    elif choice == "2":
        # Display the cart
        while True:
            cart_display()

            remove = input("\nWhich item would you like to remove (1-3):\n"
                           "To return to the main menu, "
                           "please enter zero (0):\n")


            try:
                # Give the option to return to main menu,
                # in case above selection was by mistake.
                if remove == "0":
                    break

                # Correct indexing
                removed_item = int(remove) - 1

                # Find item that must be removed and
                # check that it's in the cart.
                if quant[removed_item] > 1:
                    quant[removed_item] -= 1
                    cart_total -= prices[removed_item]

                    print(f"\n{items[removed_item]} has been removed "
                          f"from the cart successfully.")
                    break

                else:
                    quant[removed_item] -= 1
                    cart_total -= prices[removed_item]

                    print(f"\n{items[removed_item]} has been removed "
                          f"from the cart successfully.")
                    remove_item()
                    break

            except IndexError:
                length_items()
            except ValueError:
                length_items()
            except Exception as e:
                print("An unexpected error occurred:", e)


    elif choice == "3":
        # Calculate the total cost of the cart
        total_cost = round(cart_total, 2)

        print(f"The total cost of your shopping cart is £{total_cost}.")


    elif choice == "4":
        # Exit from the program
        print("\nThank you for shopping with Paws n Cart!")
        done = True


    else:
        print("That is not a valid option.")
