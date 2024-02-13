order = [
    {"name": "Burger", "price": 1.50},
    {"name": "Fries", "price": 2.50},
    {"name": "Drink", "price": 1.75},
    {"name": "Combo", "price": 5.00}
]

# Function to call the list of available menu items
def print_items():
    print("Available Items:")
    for i, item in enumerate(order, 1):
        print(f"{i}. {item['name']}: ${item['price']}")

# Calculate the total for price
def calculate_total(selected_order):
    total = sum(order[i - 1]["price"] for i in selected_order)
    return total

# Calculate the tax amount based on the total
def calculate_tax(total):
    tax_rate = 0.0485 # Set tax rate to the state of Utah
    return total * tax_rate

# Boolean for Tip choice
def tip(chosen_tip):
    return chosen_tip.lower() == "yes" or chosen_tip.lower() == "y"

# This is the heart of the program, it puts everything together and allows the user to interact with the program
def main():
    selected_order = []
    while True:
        print_items()
        print("Enter the number of the item you want to add to the receipt (0 to finish):")
        try:
            choice = int(input())
            if choice == 0:
                break
            elif choice < 1 or choice > len(order):
                print("Invalid choice. Please enter a valid item number.")
            else:
                selected_order.append(choice)
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    
    tip_choice = input("Would you like to leave a tip of 20%? (yes/no): ")
    include_tip = tip(tip_choice)
    
    if not selected_order:
        print("No items selected. Receipt is empty.")
    else:
        total = calculate_total(selected_order)
        tip_percentage = 0.2
        tip_amount = total * tip_percentage  
        
        if include_tip:
            total += tip_amount
        
        tax_amount = calculate_tax(total)
        total += tax_amount
        
        print()
        print("Receipt:")
        for choice in selected_order:
            item = order[choice - 1]
            print(f"{item['name']}: ${item['price']}")

        print()
        if include_tip:
            print(f"Tip: ${tip_amount:.2f}")
        print(f"Tax: ${tax_amount:.2f}")
        print()
        print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()

