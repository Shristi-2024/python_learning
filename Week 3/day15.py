# Contact Book
contacts = {}

def create_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"{name}: Phone = {details['phone']}, Email = {details['email']}")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        print("Contact updated!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Create Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice. Try again.")
