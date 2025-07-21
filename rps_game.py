import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")
        master.geometry("400x400")
        master.resizable(False, False)
        master.configure(bg="#2e2e2e")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.symbols = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
        self.user_score = 0
        self.computer_score = 0

        self.font_large = ("Helvetica", 16, "bold")
        self.font_medium = ("Helvetica", 12)
        self.font_small = ("Helvetica", 10)

        # Title label
        self.title_label = tk.Label(master, text="Rock-Paper-Scissors", font=self.font_large, fg="white", bg="#2e2e2e")
        self.title_label.pack(pady=10)

        # Score label
        self.score_label = tk.Label(master, text="User: 0  Computer: 0", font=self.font_medium, fg="white", bg="#2e2e2e")
        self.score_label.pack(pady=5)

        # Frame for buttons
        self.button_frame = tk.Frame(master, bg="#2e2e2e")
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("Rock"),
                                     font=self.font_medium, bg="#007acc", fg="white", activebackground="#005f99",
                                     activeforeground="white", bd=0, relief=tk.FLAT, padx=20, pady=10)
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("Paper"),
                                      font=self.font_medium, bg="#007acc", fg="white", activebackground="#005f99",
                                      activeforeground="white", bd=0, relief=tk.FLAT, padx=20, pady=10)
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("Scissors"),
                                         font=self.font_medium, bg="#007acc", fg="white", activebackground="#005f99",
                                         activeforeground="white", bd=0, relief=tk.FLAT, padx=20, pady=10)
        self.scissors_button.grid(row=0, column=2, padx=5)

        # Result labels
        self.user_choice_label = tk.Label(master, text="Your choice: ", font=self.font_medium, fg="white", bg="#2e2e2e")
        self.user_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(master, text="Computer's choice: ", font=self.font_medium, fg="white", bg="#2e2e2e")
        self.computer_choice_label.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=self.font_large, fg="yellow", bg="#2e2e2e")
        self.result_label.pack(pady=10)

        # Play again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_round,
                                           font=self.font_medium, bg="#33cc33", fg="white", activebackground="#229922",
                                           activeforeground="white", bd=0, relief=tk.FLAT, padx=20, pady=8, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        user_symbol = self.symbols.get(user_choice, "")
        self.user_choice_label.config(text=f"Your choice: {user_symbol} {user_choice}")
        computer_choice = random.choice(self.choices)
        computer_symbol = self.symbols.get(computer_choice, "")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_symbol} {computer_choice}")

        winner = self.determine_winner(user_choice, computer_choice)
        if winner == "user":
            self.result_label.config(text="You Win!", fg="#99ff99")
            self.user_score += 1
        elif winner == "computer":
            self.result_label.config(text="You Lose!", fg="#ff6666")
            self.computer_score += 1
        else:
            self.result_label.config(text="It's a Tie!", fg="yellow")

        self.update_score()
        self.disable_choice_buttons()
        self.play_again_button.config(state=tk.NORMAL)

    def determine_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            return "user"
        else:
            return "computer"

    def update_score(self):
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

    def disable_choice_buttons(self):
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)

    def enable_choice_buttons(self):
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)

    def reset_round(self):
        self.user_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer's choice: ")
        self.result_label.config(text="")
        self.enable_choice_buttons()
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
