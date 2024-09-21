'''Start

The program begins execution.
Display Menu

Display the menu of hot dog options (Hot Dog and Chili Dog) and the available toppings (Cheese, Peppers, Grilled Onions).
Input Hot Dog Type

The user is prompted to enter the type of hot dog they want (Hot Dog or Chili Dog).
Validate Hot Dog Type

Check if the input is either "Hot Dog" or "Chili Dog".
If valid, continue; otherwise, display an error message and terminate.
Input Toppings

The user is prompted to enter any toppings they want, separated by commas. If no toppings are needed, the user can press Enter to skip.
Validate Toppings

The program checks whether the toppings entered are valid (Cheese, Peppers, Grilled Onions).
If valid, continue; otherwise, display an error message and terminate.
Calculate Base Price and Toppings Cost

Based on the user's hot dog selection, the base price is determined.
The toppings selected are summed up to determine the total cost of toppings.
Calculate Tax and Total Cost

The tax is calculated as 7% of the subtotal (base price + toppings cost).
The total cost is calculated as subtotal + tax.
Display Order Summary

Display the hot dog type, base price, toppings cost, tax, and the total cost of the order.
End'''



# Function to calculate the total cost
def calculate_total(hot_dog_price, toppings, tax_rate):
    # Calculate the total price without tax
    total_cost = hot_dog_price + sum(toppings)
    
    # Calculate tax
    tax = total_cost * tax_rate
    
    # Final total with tax
    final_total = total_cost + tax
    
    return total_cost, tax, final_total

# Main program
def hot_dog_order():
    # Prices for hot dogs and toppings
    HOT_DOG_PRICE = 3.50
    CHILI_DOG_PRICE = 4.50
    CHEESE_PRICE = 0.50
    PEPPERS_PRICE = 0.75
    ONIONS_PRICE = 1.00
    TAX_RATE = 0.07

    # Ask for hot dog type
    hot_dog_type = input("Enter the type of hot dog ('hot dog' or 'chili dog'): ").strip().lower()

    # Determine the base price of the hot dog
    if hot_dog_type == "hot dog":
        hot_dog_price = HOT_DOG_PRICE
    elif hot_dog_type == "chili dog":
        hot_dog_price = CHILI_DOG_PRICE
    else:
        print("Invalid hot dog type.")
        return

    # Ask for toppings
    toppings = []
    cheese = input("Would you like cheese? (yes/no): ").strip().lower()
    if cheese == "yes":
        toppings.append(CHEESE_PRICE)
    
    peppers = input("Would you like peppers? (yes/no): ").strip().lower()
    if peppers == "yes":
        toppings.append(PEPPERS_PRICE)
    
    onions = input("Would you like grilled onions? (yes/no): ").strip().lower()
    if onions == "yes":
        toppings.append(ONIONS_PRICE)

    # Calculate the costs
    hot_dog_cost, tax, total_cost = calculate_total(hot_dog_price, toppings, TAX_RATE)

    # Display the results
    print(f"\nHot dog cost: ${hot_dog_cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total cost: ${total_cost:.2f}")

hot_dog_order()