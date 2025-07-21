import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
import os

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title(" To-Do List")
        master.geometry("450x550")
        master.resizable(False, False)

        # Styling
        master.configure(bg="#2e2e2e")  # Dark background
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

        # Task data
        self.tasks = []  # List of dicts: {"task": str, "completed": bool}

        # --- Task Input Frame ---
        self.input_frame = tk.Frame(master, bg="#2e2e2e")
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, width=30, font=self.font_medium, bd=0, relief=tk.FLAT,
                                   bg="#4a4a4a", fg="white", insertbackground="white")
        self.task_entry.pack(side=tk.LEFT, padx=5, ipady=6)
        self.task_entry.bind("<Return>", self.add_task_event)

        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, font=self.font_medium,
                                    bg="#007acc", fg="white", activebackground="#005f99", activeforeground="white",
                                    bd=0, relief=tk.FLAT, padx=10, pady=5)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # --- Task List Frame ---
        self.list_frame = tk.Frame(master, bg="#2e2e2e")
        self.list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(self.list_frame, width=40, height=18, font=self.font_medium, bd=0,
                                       relief=tk.FLAT, bg="#4a4a4a", fg="white", selectbackground="#007acc",
                                       selectforeground="white", highlightthickness=0)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_listbox.bind("<Double-Button-1>", self.edit_task_event)

        self.scrollbar = tk.Scrollbar(self.list_frame, command=self.task_listbox.yview, troughcolor="#2e2e2e",
                                      bg="#4a4a4a")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # --- Action Buttons Frame ---
        self.button_frame = tk.Frame(master, bg="#2e2e2e")
        self.button_frame.pack(pady=10)

        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task, font=self.font_medium,
                                     bg="#ffaa00", fg="white", activebackground="#cc8800", activeforeground="white",
                                     bd=0, relief=tk.FLAT, padx=10, pady=5)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task,
                                       font=self.font_medium, bg="#cc3333", fg="white", activebackground="#992222",
                                       activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=5)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Mark Complete", command=self.mark_complete,
                                         font=self.font_medium, bg="#33cc33", fg="white", activebackground="#229922",
                                         activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=5)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear Completed", command=self.clear_completed,
                                      font=self.font_medium, bg="#555555", fg="white", activebackground="#333333",
                                      activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=5)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # --- Save/Load Buttons Frame ---
        self.save_load_frame = tk.Frame(master, bg="#2e2e2e")
        self.save_load_frame.pack(pady=5)

        self.save_button = tk.Button(self.save_load_frame, text="Save Tasks", command=self.save_tasks,
                                     font=self.font_small, bg="#007acc", fg="white", activebackground="#005f99",
                                     activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=3)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.save_load_frame, text="Load Tasks", command=self.load_tasks,
                                     font=self.font_small, bg="#007acc", fg="white", activebackground="#005f99",
                                     activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=3)
        self.load_button.pack(side=tk.LEFT, padx=5)

        # Load tasks on startup if file exists
        self.default_save_file = "tasks.json"
        if os.path.exists(self.default_save_file):
            self.load_tasks(self.default_save_file)

    def add_task_event(self, event=None):
        self.add_task()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task_event(self, event=None):
        self.edit_task()

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.tasks[selected_index]["task"]
            new_task = simpledialog.askstring("Edit Task", "Modify the selected task:", initialvalue=current_task)
            if new_task is not None:
                new_task = new_task.strip()
                if new_task:
                    self.tasks[selected_index]["task"] = new_task
                    self.update_task_listbox()
                else:
                    messagebox.showwarning("Warning", "Task cannot be empty.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected task?")
            if confirm:
                del self.tasks[selected_index]
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            if not task["completed"]:
                task["completed"] = True
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark complete.")

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["task"]
            if task["completed"]:
                display_text = "✓ " + display_text
            self.task_listbox.insert(tk.END, display_text)
            if task["completed"]:
                self.task_listbox.itemconfig(tk.END, fg="#99ff99")  # Green color for completed tasks

    def save_tasks(self, filename=None):
        if filename is None:
            filename = self.default_save_file
        try:
            with open(filename, "w") as f:
                json.dump(self.tasks, f)
            messagebox.showinfo("Save Successful", f"Tasks saved to {filename}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save tasks: {e}")

    def load_tasks(self, filename=None):
        if filename is None:
            filename = self.default_save_file
        try:
            with open(filename, "r") as f:
                self.tasks = json.load(f)
            self.update_task_listbox()
            messagebox.showinfo("Load Successful", f"Tasks loaded from {filename}")
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load tasks: {e}")

    def minimize_window(self):
        self.master.iconify()

    def toggle_maximize(self):
        if self.master.state() == "normal":
            self.master.state("zoomed")
        else:
            self.master.state("normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
