import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and number:
        contacts[name] = {"Number": number, "Email": email, "Address": address}
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and Number are required fields.")

# Function to view contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"Name: {name}, Number: {info['Number']}, Email: {info['Email']}, Address: {info['Address']}")

# Function to search for a contact
def search_contact():
    name = name_entry.get()
    if name in contacts:
        info = contacts[name]
        result_label.config(text=f"Name: {name}, Number: {info['Number']}, Email: {info['Email']}, Address: {info['Address']}")
    else:
        result_label.config(text="Contact not found")

# Function to update a contact
def update_contact():
    name = name_entry.get()
    if name in contacts:
        number = number_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        contacts[name] = {"Number": number, "Email": email, "Address": address}
        clear_entries()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Contact not found")

# Function to delete a contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact not found")

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create input fields
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
number_label = tk.Label(root, text="Number:")
number_entry = tk.Entry(root)
email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)
address_label = tk.Label(root, text="Address:")
address_entry = tk.Entry(root)

name_label.pack()
name_entry.pack()
number_label.pack()
number_entry.pack()
email_label.pack()
email_entry.pack()
address_label.pack()
address_entry.pack()

# Create buttons for actions
add_button = tk.Button(root, text="Add Contact", command=add_contact)
view_button = tk.Button(root, text="View Contacts", command=view_contacts)
search_button = tk.Button(root, text="Search Contact", command=search_contact)
update_button = tk.Button(root, text="Update Contact", command=update_contact)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)

add_button.pack()
view_button.pack()
search_button.pack()
update_button.pack()
delete_button.pack()

# Create a listbox for viewing contacts
contact_list = tk.Listbox(root)
contact_list.pack()

# Create a label for displaying search results
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
