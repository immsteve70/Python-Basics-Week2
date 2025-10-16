contacts = {
    "Tharane" : "01673739356",
    "Joycelyn" : "0127084599",
    "Rehma" : "01154324321",
    "Shasha" : "01111000709",
    "Brave" : "0178809832",
    "YavinHensem" : "0145612330",
    "Emmanuel" : "01164513328"
}

def add_cont():
    add_actionkey = input("Enter the contact name: ")
    add_actionvalue = input("Enter the contact number: ")
    contacts[add_actionkey] = add_actionvalue
    print("Updated Contact List:", contacts)

def remove_cont():
    print(contacts)
    remove_action = input("Which contact do you want to remove?: ")
    del contacts[remove_action]
    print("Updated Contact List:", contacts)

def search_cont():
    search_action = input("Name: ")
    print(contacts[search_action])

def view_cont():
    print("\n--- Contact List ---")
    for name, number in contacts.items():
        print(f"{name}: {number}")
    print("--------------------")


print("Welcome to the USUAL CONTACT BOOK!")

while True:
    print("Options:\n1.Add new contact\n2.Remove contact\n3.Search by name\n4.View all contacts\n5.Exit")
    action = int(input("Choose your option: "))

    if action == 1:
        add_cont()
    elif action == 2:
        remove_cont()
    elif action == 3:
        search_cont()
    elif action == 4:
        view_cont()
    elif action == 5:
        print("Goodbyeee!!!")
        break
    else:
        print("Invalid response")
        continue
