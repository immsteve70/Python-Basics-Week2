groceriesitem = {
    "Rice" : 50.10,
    "Milk" : 27.99,
    "Maggi" : 8.59,
    "Powder" : 12.70,
    "Fish" : 25.00
}

cart = []

def add_item():
    print(groceriesitem)
    add_item_action = input("Choose the item you want to add: ")
    cart.append(add_item_action)
    print(f"{add_item_action} has been added to cart!")

def remove_item():
    print(cart)
    remove_item_action = input("Choose the item you want to remove: ")
    cart.remove(remove_item_action)
    print(f"{remove_item_action} has been removed from the cart!")

def view_cart():
    for num, grocery in enumerate(cart, 1):
        print(f"{num}. {grocery}\n")

def total_cost():
    total = 0
    for item in cart:
        price = (groceriesitem[item])
        total += price
    print(f"Total cost: RM{total:.2f}")

print("Welcome to the USUAL GROCERY STORE!")

while True:
    print("1. Add Items\n2.Remove Items\n3.View cart\n4.Total cost\n5.Exit")
    action = int(input("Choose your option: "))

    if action == 1:
        add_item()
    elif action == 2:
        remove_item()
    elif action == 3:
        view_cart()
    elif action == 4:
        total_cost()
    elif action == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid response!")

    