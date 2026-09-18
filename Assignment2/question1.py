# Interactive Terminal E-Commerce Cart & Inventory Tracker
catalog = {
    "laptop": 800,
    "mouse": 20,
    "keyboard": 50,
    "monitor": 150
}


grand_total = 0 # variable to store the total price
print(catalog)  #printing the catalog for the user to see available items
while True:
    item = input("Enter item to buy (or 'checkout' / 'exit'): ").lower() 
   
    if item == "exit":
        print("--> Order cancelled. Goodbye!")
        break


    elif item == "checkout":

        # Apply conditional discounts
        if grand_total >= 500:
            discount_rate = 0.10

        elif grand_total >= 200 and grand_total < 500:
            discount_rate = 0.05

        elif grand_total < 200:
            discount_rate = 0

        elif grand_total == 0:
            print("--> No items in the cart. Please add items before checkout.")
            continue

        # Calculate the discount amount
        discount = grand_total * discount_rate 

        # Calculate the final bill
        final_total = grand_total - discount

        print("\nCHECKOUT RECEIPT")
        print("======================================")
        print(f"Subtotal:     ${grand_total:.1f}")
        print(f"Discount:     ${discount:.1f}")
        print(f"Final Total:  ${final_total:.1f}")
        print("======================================")
       
        break  # Exit the loop after checkout

    elif item in catalog:

        price = catalog[item]  # Get the price of the selected item

        grand_total += price # Add the price to the running total

        print(f"--> Added {item} (${price}) to order.") # Print confirmation

    else:
        print(
            "--> [ERROR] Item not found in catalog. "
            "Try again."
        )