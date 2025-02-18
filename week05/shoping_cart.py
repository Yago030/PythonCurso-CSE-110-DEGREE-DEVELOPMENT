"""
Author: Santiago Bergerat  
Team Activity: Shopping Cart  

Welcome to your interactive shopping cart!  
Here, you can add products, view your list, remove items, and calculate the total cost of your purchase.  
Manage your shopping easily and efficiently!  
"""

cart_items = []
cart_prices = []

while True:
    print("\n1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")



    choice = input("Choose an option: ")



    if choice == "1":
        cart_items.append(input("Item: "))
        cart_prices.append(float(input("Price: ")))



    elif choice == "2":
        if cart_items:
            print("\nShopping Cart:")
            for i in range(len(cart_items)):
                print(f"{i + 1}. {cart_items[i]} - ${cart_prices[i]:.2f}")
        else:
            print("\nYour cart is empty.")



    elif choice == "3":
        if cart_items:
            for i in range(len(cart_items)):
                print(f"{i + 1}. {cart_items[i]} - ${cart_prices[i]:.2f}")
            index = int(input("Remove item number: ")) - 1
            if 0 <= index < len(cart_items):
                removed_item = cart_items.pop(index)
                removed_price = cart_prices.pop(index)
                print(f"{removed_item} removed from cart.")
            else:
                print("Invalid selection.")
        else:
            print("\nYour cart is empty. Nothing to remove.")



    elif choice == "4":
        print(f"\nTotal: ${sum(cart_prices):.2f}")



    elif choice == "5":
        print("\nFinal cart summary:")
        if cart_items:
            for i in range(len(cart_items)):
                print(f"{i + 1}. {cart_items[i]} - ${cart_prices[i]:.2f}")
            print(f"\nTotal: ${sum(cart_prices):.2f}")
        else:
            
            print("Your cart is empty.")

        print("\nThank you for using the shopping cart. Goodbye!")
        
        break

    else:
        
        print("Invalid choice. Please select a valid option.")
