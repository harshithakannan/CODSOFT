import tkinter as tk
from PIL import Image, ImageTk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors Game Window")
root.geometry("400x600")
root.config(bg="#8EE5EE")
rock_img = Image.open("rock.png")
paper_img = Image.open("paper.png")
scissors_img = Image.open("scissors.png")

rock_img = ImageTk.PhotoImage(rock_img.resize((100, 100)))
paper_img = ImageTk.PhotoImage(paper_img.resize((100, 100)))
scissors_img = ImageTk.PhotoImage(scissors_img.resize((100, 100)))

choices = ["rock", "paper", "scissors"]
images = {"rock": rock_img, "paper": paper_img, "scissors": scissors_img}


# Scores
user_score = 0
comp_score = 0

def user_choice(user_input):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    user_choice_label.config(image=images[user_input])
    comp_choice_label.config(image=images[comp_choice])
    result = check_winner(user_input, comp_choice)
    result_label.config(text=result, bg="#A52A2A")
    update_scores(result)
    play_again_button.grid(row=6, column=0, columnspan=3, pady=10)
    end_game_button.grid(row=7, column=0, columnspan=3, pady=10)

def check_winner(user, comp):
    if user == comp:
        return "It's a tie!"
    elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
        return "You win!"
    else:
        return "You lose!"

def update_scores(result):
    global user_score, comp_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        comp_score += 1
    user_score_label.config(text=f"Your Score: {user_score}")
    comp_score_label.config(text=f"Computer's Score: {comp_score}")

def play_again():
    user_choice_label.config(image='')
    comp_choice_label.config(image='')
    result_label.config(text="")
    play_again_button.grid_remove()
    end_game_button.grid_remove()

def end_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    comp_score_label.config(text=f"Computer's Score: {comp_score}")
    play_again()

# Labels
user_label = tk.Label(root, text="Your choice:", bg="#EEC591")
user_choice_label = tk.Label(root)
vs_label = tk.Label(root, text="VS", bg="#EEC591")
comp_label = tk.Label(root, text="Computer's choice:", bg="#EEC591")
comp_choice_label = tk.Label(root)
result_label = tk.Label(root, text="", font=("Arial", 16))
user_score_label = tk.Label(root, text="Your Score: 0", bg="#FFB6C1", font=("Arial", 14))
comp_score_label = tk.Label(root, text="Computer's Score: 0", bg="#FFB6C1", font=("Arial", 14))

user_label.grid(row=0, column=0, padx=10, pady=10)
user_choice_label.grid(row=1, column=0, padx=10, pady=10)
vs_label.grid(row=1, column=1, padx=10, pady=10)
comp_label.grid(row=0, column=2, padx=10, pady=10)
comp_choice_label.grid(row=1, column=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=3, pady=10)
user_score_label.grid(row=3, column=0, columnspan=3, pady=5)
comp_score_label.grid(row=4, column=0, columnspan=3, pady=5)

# Buttons
rock_button = tk.Button(root, image=rock_img, command=lambda: user_choice("rock"))
paper_button = tk.Button(root, image=paper_img, command=lambda: user_choice("paper"))
scissors_button = tk.Button(root, image=scissors_img, command=lambda: user_choice("scissors"))

# P0lay again
play_again_button = tk.Button(root, text="Play Again", bg="#E3CF57", command=play_again)

# End game
end_game_button = tk.Button(root, text="End Game", bg="#E3CF57", command=end_game)

rock_button.grid(row=5, column=0, padx=10, pady=10)
paper_button.grid(row=5, column=1, padx=10, pady=10)
scissors_button.grid(row=5, column=2, padx=10, pady=10)

# Hide the play again and end game buttons initially
play_again_button.grid_remove()
end_game_button.grid_remove()


root.mainloop()
