import tkinter as tk
#import gpiozero
#from gpiozero import Button
import random
options = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
keyoptions = ("r", "p", "s", "l", "v", "a")
results = (
    ("You & Teddy Tie", "Teddy Wins", "You Win!", "You Win!", "Teddy Wins", "Rock"),
("You Win!", "You & Teddy Tie", "Teddy Wins", "Teddy Wins", "You Win!", "Paper"),
("Teddy Wins", "You Win!", "You & Teddy Tie", "You Win!", "Teddy Wins", "Scissors"),
("Teddy Wins", "You Win!", "Teddy Wins", "You & Teddy Tie", "You Win!", "Lizard"),
("You Win!", "Teddy Wins", "You Win!", "Teddy Wins", "You & Teddy Tie", "Spock")
)
result_dict = {"r":0, "p":1, "s":2, "l":3, "v":4}


def play_rpsls():
    teddy_move = random.randint(0,4)
    player_move = input("press: r, p, s, l, or v\n")
    if player_move not in ["r", "p", "s", "l", "v" #, "a"
    ]:
        print("please enter a valid key: r, p, s, l, or, v")
        play_rpsls()
    #elif player_move == "a":
        #print("Hi Pippin You Auto Win!!! Also Austin sucks and ill blend him for you :)")
    else:
        #print(teddy_move)
        #print(player_move)
        player_move_index = keyoptions.index(player_move)
        #print(player_move_index)
        print("Teddy Played " + options[teddy_move] + " You Played " + options[player_move_index] + " So " + results[player_move_index][teddy_move]) 

play_rpsls()


#https://gpiozero.readthedocs.io/en/stable/
