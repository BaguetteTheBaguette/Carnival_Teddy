
import random
from teddy_arm_control import cheer
from button_control import button_pressed

options = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
keyoptions = ("r", "p", "s", "l", "v")
tie_ = "You & Teddy Tie" # _ added so variables have same characters
lose = "Teddy Wins"
win_ = "You Win!"
results = (
(tie_, lose, win_, win_, lose, "Rock"),
(win_, tie_, lose, lose, win_, "Paper"),
(lose, win_, tie_, win_, lose, "Scissors"),
(lose, win_, lose, tie_, win_, "Lizard"),
(win_, lose, win_, lose, tie_, "Spock")
)
#result_dict = {"r":0, "p":1, "s":2, "l":3, "v":4} #sets each key to an integer this way results can be indexed to determine the game result


def play_rpsls():
    teddy_move = random.randint(0,4) # picks random number for teddy's move
    player_move = input("press: r, p, s, l, or v\n") #waits for player input and displays possible keys, will be changed to wait for button input later
    if player_move not in ["r", "p", "s", "l", "v" ]: # checks a valid key was pressed
        print("please enter a valid key: r, p, s, l, or, v") # displays a message telling player to press a valid key, wont be a problem with buttons
        play_rpsls() # recalls function until player enters valid key, wont be a problem with buttons
    
    else:
        player_move_index = keyoptions.index(player_move) # finds the integer corresponding to the key the player clicked
        result = results[player_move_index][teddy_move] # finds result of game based on player and teddy move
        print("Teddy Played " + options[teddy_move] + " & You Played " + options[player_move_index] + " So " + result ) # prints result
        if result == lose: # checks if player lost
            cheer() # calls cheer will matter more later



play_rpsls() #runs this function



