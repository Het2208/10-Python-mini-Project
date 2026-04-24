# Objective
#
# Store name & phone numbers, allow:
#
# Add contact
#
# Search by name
#
# Delete contact
#
# Display all
#
# Concepts Learned
#
# ✔ Dictionaries
# ✔ CRUD operations
# ✔ While loops
# ✔ Menu-based program
# ✔ Data validation


def readContact(contacts):
    print("-" * 30)
    if not contacts:
        print("No contacts found!")
    else:
        for name, phone in contacts.items():
            print(f"{name} => {phone}")
    print("-" * 30)

def addContact(contacts , name , phone):
    print("-" * 30)
    contacts[name] = phone
    print(f"Contact Added | Name: {name} | Phone: {phone}")
    print("-" * 30)

def editContact(contacts , name , phone):
    print("-" * 30)
    contacts[name] = phone
    print(f"Contact Updated | Name: {name} | Phone: {phone}")
    print("-" * 30)

def deleteContact(contacts , name):
    print("-" * 30)
    del contacts[name]
    print(f"Contact Deleted | Name: {name}")
    print("-" * 30)

def main():
    print("*"*30)
    print("Welcome to Contact Book")
    print("*"*30)

    Contacts = {}
    is_exit = True

    while is_exit:

        print("\n1. Read All Contact\n2. Add Contact\n3. Edit Contact\n4. Delete Contact\n5. Exit")
        ch = int(input("\nEnter your choice: "))

        match ch:
            case 1:
                readContact(Contacts)

            case 2:
                name = input("Enter name to add: ")
                phone = input("Enter 10 digit phone number: ")
                while len(phone) != 10:
                    phone = input("Enter valid 10 digit phone number: ")
                addContact(Contacts, name, phone)

            case 3:
                name = input("Enter name to edit: ")
                if name in Contacts:
                    phone = input("Enter new 10 digit phone number: ")
                    while len(phone) != 10:
                        phone = input("Enter valid 10 digit phone number: ")
                    editContact(Contacts, name, phone)
                else:
                    print(f"{name} not found!")

            case 4:
                name = input("Enter name to delete: ")
                if name in Contacts:
                    deleteContact(Contacts, name)
                else:
                    print(f"{name} not found!")

            case 5:
                is_exit = False

            case _:
                print("Invalid Choice!")

main()
