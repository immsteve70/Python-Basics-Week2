grocery_list = []

try:
    with open("groceries.txt", "r") as file:
        for line in file:
            grocery_list.append(line.strip())
except FileNotFoundError:
    grocery_list = []

def add_item():
    item = input("What item do you want to add?: ")
    grocery_list.append(item)
    print(f"{item} has been added to the list.\n")
    save_list()
    
def remove_item():
    item = input("What item do you want to remove?: ")
    grocery_list.remove(item)
    print(f"{item} has been removed from the list.\n")
    save_list()
    
def show_list():
    for num, grocery in enumerate(grocery_list, 1):
        print(f"{num}. {grocery}\n")

def save_list():
    with open("groceries.txt", "w") as file:
        for item in grocery_list:
            file.write(item + "\n")

while True:
    print("1.Add Item\n2.Remove Item\n3.View List\n4.Exit")
    action = int(input("Choose your option: "))

    if action == 1:
        add_item()
    elif action == 2:
        remove_item()
    elif action == 3:
        show_list()
    elif action == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid Response\n")
    
    



