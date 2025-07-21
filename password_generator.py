import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x300")
        master.resizable(False, False)
        master.configure(bg="#2e2e2e")

        self.font_large = ("Helvetica", 16, "bold")
        self.font_medium = ("Helvetica", 12)
        self.font_small = ("Helvetica", 10)

        # --- Window Control Frame ---
        self.window_control_frame = tk.Frame(master, bg="#2e2e2e")
        self.window_control_frame.pack(side=tk.TOP, anchor="ne", padx=5, pady=5)

        self.minimize_button = tk.Button(self.window_control_frame, text="_", command=self.minimize_window,
                                         font=self.font_large, bg="#555555", fg="white", activebackground="#333333",
                                         activeforeground="white", bd=0, relief=tk.FLAT, padx=8, pady=2)
        self.minimize_button.pack(side=tk.LEFT, padx=2)

        self.maximize_button = tk.Button(self.window_control_frame, text="▢", command=self.toggle_maximize,
                                         font=self.font_large, bg="#555555", fg="white", activebackground="#333333",
                                         activeforeground="white", bd=0, relief=tk.FLAT, padx=8, pady=2)
        self.maximize_button.pack(side=tk.LEFT, padx=2)

        # Title label
        self.title_label = tk.Label(master, text="Password Generator", font=self.font_large, fg="white", bg="#2e2e2e")
        self.title_label.pack(pady=10)

        # Frame for input
        self.input_frame = tk.Frame(master, bg="#2e2e2e")
        self.input_frame.pack(pady=10)

        self.length_label = tk.Label(self.input_frame, text="Password Length:", font=self.font_medium, fg="white", bg="#2e2e2e")
        self.length_label.grid(row=0, column=0, padx=5, sticky="w")

        self.length_entry = tk.Entry(self.input_frame, width=5, font=self.font_medium, bd=0, relief=tk.FLAT,
                                     bg="#4a4a4a", fg="white", insertbackground="white")
        self.length_entry.grid(row=0, column=1, padx=5, sticky="w")
        self.length_entry.insert(0, "12")

        # Character type checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        self.uppercase_check = tk.Checkbutton(self.input_frame, text="Uppercase", variable=self.uppercase_var,
                                              font=self.font_small, fg="white", bg="#2e2e2e", activebackground="#2e2e2e",
                                              activeforeground="white", selectcolor="#2e2e2e")
        self.uppercase_check.grid(row=1, column=0, sticky="w", padx=5)

        self.lowercase_check = tk.Checkbutton(self.input_frame, text="Lowercase", variable=self.lowercase_var,
                                              font=self.font_small, fg="white", bg="#2e2e2e", activebackground="#2e2e2e",
                                              activeforeground="white", selectcolor="#2e2e2e")
        self.lowercase_check.grid(row=1, column=1, sticky="w", padx=5)

        self.digits_check = tk.Checkbutton(self.input_frame, text="Digits", variable=self.digits_var,
                                           font=self.font_small, fg="white", bg="#2e2e2e", activebackground="#2e2e2e",
                                           activeforeground="white", selectcolor="#2e2e2e")
        self.digits_check.grid(row=2, column=0, sticky="w", padx=5)

        self.symbols_check = tk.Checkbutton(self.input_frame, text="Symbols", variable=self.symbols_var,
                                            font=self.font_small, fg="white", bg="#2e2e2e", activebackground="#2e2e2e",
                                            activeforeground="white", selectcolor="#2e2e2e")
        self.symbols_check.grid(row=2, column=1, sticky="w", padx=5)

        # Complexity scale label and slider
        self.complexity_label = tk.Label(master, text="Complexity Scale:", font=self.font_medium, fg="white", bg="#2e2e2e")
        self.complexity_label.pack(pady=(10, 0))

        self.complexity_scale = tk.Scale(master, from_=1, to=5, orient=tk.HORIZONTAL, bg="#2e2e2e", fg="white",
                                         troughcolor="#4a4a4a", highlightthickness=0, length=200)
        self.complexity_scale.set(3)
        self.complexity_scale.pack()

        # Generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password,
                                         font=self.font_medium, bg="#007acc", fg="white", activebackground="#005f99",
                                         activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=5)
        self.generate_button.pack(pady=10)

        # Password display
        self.password_display = tk.Entry(master, font=self.font_medium, bd=0, relief=tk.FLAT,
                                         bg="#4a4a4a", fg="white", justify=tk.CENTER, width=30)
        self.password_display.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer for password length.")
            return

        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Invalid Selection", "Please select at least one character type.")
            return

        # Adjust length based on complexity scale (scale 1-5 multiplies length by 0.5 to 1.5)
        complexity = self.complexity_scale.get()
        adjusted_length = max(1, int(length * (0.5 + 0.25 * complexity)))

        password = ''.join(random.choice(characters) for _ in range(adjusted_length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

    def minimize_window(self):
        self.master.iconify()

    def toggle_maximize(self):
        if self.master.state() == "normal":
            self.master.state("zoomed")
        else:
            self.master.state("normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
