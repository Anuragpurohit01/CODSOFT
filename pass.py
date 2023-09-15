import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_scale.get()
    complexity = complexity_scale.get()

    if length <= 0:
        messagebox.showinvalid("invalid", "Length of Password  must be greater than zero.")
        return

    if complexity <= 0:
        messagebox.showinvalid("invalid", "Password complexity must be greater than zero.")
        return

    characters = ""
    if complexity >= 1:
        characters += string.ascii_letters
    if complexity >= 2:
        characters += string.digits
    if complexity >= 3:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def reset_password():
    length_scale.set(8)
    complexity_scale.set(1)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator by Anurag")

# Heading
heading_label = tk.Label(root, text="Password Generator by Anurag", font=("bold", 20))
heading_label.pack(pady=10)


# Password Length Entry
length_label = tk.Label(root, text=" Length of Password :",font=("bold", 16))
length_label.pack()
length_scale = tk.Scale(root, from_=1, to=50, orient=tk.HORIZONTAL, length=200,bg="grey")
length_scale.set(8)
length_scale.pack(pady=5)

# Password Complexity Entry
complexity_label = tk.Label(root, text="Password Complexity:",font=("bold", 16))
complexity_label.pack()
complexity_scale = tk.Scale(root, from_=1, to=3, orient=tk.HORIZONTAL, length=200,bg="grey")
complexity_scale.set(1)
complexity_scale.pack(pady=5)

# Generate Password Button
generate_button = tk.Button(root, text="Generate the Password",bg="blue", command=generate_password)
generate_button.pack(pady=10)

# Password Display
password_label = tk.Label(root, text="Password:",font=("bold", 20))
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack(pady=5)

# Reset Password Button
reset_button = tk.Button(root, text="Reset Password", command=reset_password,bg="red")
reset_button.pack(pady=10)

root.mainloop()