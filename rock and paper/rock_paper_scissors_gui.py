import tkinter as tk
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}.\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=15)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

tk.Button(root, text="Reset Game", command=reset_game).pack(pady=10)

root.mainloop()
