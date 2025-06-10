import pickle
import os
from tkinter import Tk, filedialog

phonebook = {}

def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("Invalid input. Name cannot be empty.")
        return
    number = input("Enter number: ").strip()
    if not number.isdigit():
        print("Invalid input. Phone number must contain only digits.")
        return
    phonebook[name] = number
    print(f"Added {name}: {number}")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name}")
    else:
        print(f"{name} not found in phonebook.")

def find_contact():
    name = input("Enter name to find: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook.")

def save_contacts():
    filename = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])
    if filename:
        if os.path.exists(filename):
            print("File already exists. Choose a different name or overwrite the file.")
            overwrite = input("Do you want to overwrite the file? (y/n): ").lower()
            if overwrite != 'y':
                return
        with open(filename, 'wb') as f:
            pickle.dump(phonebook, f)
        print("Contacts saved to file.")


def load_contacts():
    filename = filedialog.askopenfilename(filetypes=[("Pickle files", "*.pkl")])
    print(filename)
    if filename:
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                global phonebook
                phonebook = pickle.load(f)
                print(phonebook)
            print("Contacts loaded from file.")
        else:
            print("File does not exist.")

def print_contacts():
    if phonebook:
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

def menu():
    root = Tk()
    root.withdraw()  # Hide Tkinter GUI window

    while True:
        print("\nPhonebook Manager")
        print('Press "a" to add a new contact.')
        print('Press "d" to delete a contact.')
        print('Press "f" to find a contact.')
        print('Press "s" to save all contacts to a file.')
        print('Press "l" to load previously saved contacts from a file.')
        print('Press "p" to print out all contacts in the phonebook.')
        print('Press "q" to quit.')

        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            add_contact()
        elif choice == 'd':
            delete_contact()
        elif choice == 'f':
            find_contact()
        elif choice == 's':
            save_contacts()
        elif choice == 'l':
            load_contacts()
        elif choice == 'p':
            print_contacts()
        elif choice == 'q':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
