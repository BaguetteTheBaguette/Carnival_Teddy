import tkinter as tk
import random
options = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
keyoptions = ("r", "p", "s", "l", "v")
results = (
    ("Tie", "Teddy Wins", "You Win!", "You Win!", "Teddy Wins", "Rock"),
("You Win!", "Tie", "Teddy Wins", "Teddy Wins", "You Win!", "Paper"),
("Teddy Wins", "You Win!", "Tie", "You Win!", "Teddy Wins", "Scissors"),
("Teddy Wins", "You Win!", "Tie", "Teddy Wins", "You Win!", "Lizard"),
("You Win!", "Teddy Wins", "You Win!", "Teddy Wins", "Tie", "Spock")
)
result_dict = {"r":0, "p":1, "s":2, "l":3, "s":4}


def play_rpsls():
    teddy_move = random.randint(0,4)
    player_move = input("press: r, p, s, l, or v")
    player_move_index = keyoptions.index(player_move)
    if player_move not in ["r", "p", "s", "l", "v"]:
        print("please enter a valid key: r, p, s, l, or, v")
        play_rpsls()
    else:
        print(teddy_move)
        print(player_move)
        print(player_move_index)
        print("Teddy Played " + options[teddy_move] + " You Played " + options[player_move_index] + " So " + results[player_move_index][teddy_move]) 

play_rpsls()