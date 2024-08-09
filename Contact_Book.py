import json
import re

FILENAME = 'contacts.json'

def load_contacts():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent="\t")

def check_phone(phone):
    return re.match(r'^09\d{9}$', phone)

def check_email(email):
    return re.match(r'^\w+@[a-z]+\.\w{3}$', email)

def add_contact(contacts):
    name = input("Enter name: ")


def add_contact(contacts):
    name = input("Enter name: ")

    while True:
        phone = input("Enter phone number: ")
        if not check_phone(phone):
            print("Invalid phone format.")
            continue
        else:
            break

    while True:
       email = input("Enter email: ")
       if not check_email(email):
          print("Invalid email format.")
          continue
       else:
           break


    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added.")


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact['name'] == name:
            new_name = input(f"Enter new name (current: {contact['name']}): ")
            while True:
                new_phone = input(f"Enter new phone number (current: {contact['phone']}): ")
                if not check_phone(new_phone):
                    print("Invalid phone format.")
                    continue
                else:
                    break

            while True:
                new_email = input(f"Enter new email (current: {contact['email']}): ")
                if not check_email(new_email):
                    print("Invalid email format.")
                    continue
                else:
                    break
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted.")
            return
    print("Contact not found.")

def show_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def sort_contacts(contacts):
    contacts.sort(key=lambda contact: contact['name'])
    save_contacts(contacts)
    print("Contacts sorted.")
    show_contacts(contacts)



def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Show Contacts")
        print("5. Sort Contacts")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            show_contacts(contacts)
        elif choice == '5':
            sort_contacts(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
