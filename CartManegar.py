shopping_cart=[]
counter=0
print("Add items")
for i in range(1,5):
    item = input("Enter the item to add: ")
    shopping_cart.append(item)
    print(item, "has been added successfully")
    counter=counter+1

print("Total number of items added:",counter)

while True:
    operation = int(input("\nChoose an operation: 1.Remove item 2.View all items 3.Clear shopping cart 4.Exit: "))

    if operation == 1:
        print("\nCurrent shopping cart:", shopping_cart)
        choice = int(input("Enter the index number (starting from 0) of the item to remove: "))
        if 0 <= choice < len(shopping_cart):
            removed_item = shopping_cart.pop(choice)
            print(removed_item, "has been removed successfully")
        else:
            print("Invalid index. Please try again.")

    elif operation == 2:
        print("\nItems in your shopping cart:", shopping_cart)

    elif operation == 3:
        shopping_cart.clear()
        print("Shopping cart has been cleared successfully")

    elif operation == 4:
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid operation. Please choose again.")



