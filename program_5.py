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



def calculate_hot_dog_cost(hot_dog_type, toppings):
    hot_dog_prices = {"Hot Dog": 3.50, "Chilling Dog": 4.50}
    topping_prices = {"cheese": 0.5, "pepper": 0.75, "grilled onions":1}
    tax_rate = 0.07
    base_price = hot_dog_prices[hot_dog_type]
    topping_cost = sum(topping_prices[topping] for topping in toppings)
    subtotal = base_prices + topping_cost
    tax = subtotal * tax_rate
    total_cost = subtotal + tax
    return base_price, topping_cost, tax, total_cost

def main():
    print("Menu:")
    print("1. Hot Dog ($3.50)")
    print("2. Chili Dog ($4.50)")
    print("Toppings: Cheese ($0.50), Peppers ($0.75), Grilled Onions ($1.00)")
    hot_dog_choice = input("Enter the type of hot dog (Hot Dog/Chili Dog): ").strip().title()

    if hot_dog_choice not in ["Hot Dog", "Chili Dog"]:
        print("Invalid choice. Please select either 'Hot Dog' or 'Chili Dog'.")
        return

    toppings_input = input("Enter toppings (separate by commas) or press Enter for no toppings (cheese, peppers, grilled onions): ").strip().lower()
    
    
    if toppings_input:
        toppings = [topping.strip() for topping in toppings_input.split(",")]
        valid_toppings = ["cheese", "peppers", "grilled onions"]
        for topping in toppings:
            if topping not in valid_toppings:
                print(f"Invalid topping: {topping}. Please select from {valid_toppings}.")
                return
    else:
        toppings = []
    

    base_price, toppings_cost, tax, total_cost = calculate_hot_dog_cost(hot_dog_choice, toppings)
    

    print(f"\n--- Order Summary ---")
    print(f"Hot Dog Type: {hot_dog_choice}")
    print(f"Base Price: ${base_price:.2f}")
    if toppings:
        print(f"Toppings Cost: ${toppings_cost:.2f}")
    else:
        print(f"Toppings Cost: $0.00")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

main()