"""
This is the primary file for the Pokeymanz game.
"""

### Importing ###

''' Pokeyman modules '''
from moves import *
from people import *
from pokeytypes import *
from pokeymanz import *
# from scenes import *

''' Python modules '''
import time
import os
import pickle

### End importing ###



### game_data ###

''' This dictionary contains all the player-specific information that the player
will accumulate throughout the course of the game. Saving the game stores this 
dict in a pickle; loading the game populates this dict with all the choices
previously made; if a new game is beginning, this will be populated with some
default values. '''
game_data = {}

### End game_data ###



### Saving and loading the game ###

SAVE_FILE = "savedgame.dat"

def save_game():
    with open(SAVE_FILE, 'wb') as f:
        pickle.dump(game_data, f)


def load_game():
    with open(SAVE_FILE, 'rb') as f:
        global game_data 
        game_data = pickle.load(f)

### End saving/loading ###



### game_loop(): The primary game loop ###

def game_loop():
    pass

### End game_loop(): The primary game loop ###



### new_game(): Introduction phase for a new game ###

def new_game():

    global game_data

    def interactor(message):
        os.system('clear')
        print("\n\n" + message)
        return input("\n> ")

    interactor("Welcome to the wonderful and exciting world of Pokeymanz!")
    interactor("I'm Harold Treebranch, the Loco region's very own " \
            + "Pokeyman professor!")
    interactor("Our world is inhabited by fantastical creatures known " \
            + "as Pokeymanz!")
    interactor("You're gonna be going on a grand adventure momentarily!")
    interactor("But first, let's take care of some housekeeping.")

    # Get player's name, double-check with them
    name = ''
    check = ''

    while check != 'y':
        name = interactor("What's your name?")
        check = interactor(name + "? Is that right?\n\n(y/n)")
        if check.lower() != 'y':
            interactor("Let's try again.")

    game_data['player_name'] = name

    print(game_data['player_name'])

### End new_game() ###



### main(): The initialization phase ###

def main():
    ''' Display startup text '''
    os.system('clear')
    print("\n\nPOKEYMANZ\n\n")
    print("Coded in Python 3.4 by Tanner Lake, 2015\n\n")
    print("LICENSE:")
    print("Whatever won't get me sued by Nintendo, Gamefreak, or anybody else.")
    print("I'm not making this for any financial gain.")
    print("It's just a means for learning how to write code.\n")
    input("> ")

    ''' Check for existence of SAVE_FILE. '''
    ''' If SAVE_FILE exists, display [player name], [badges], and [dex].
    Prompt user for LOAD/NEW.
        If LOAD: Populate game_date from SAVE_FILE and run game.
        If NEW: Start a new game.'''
    ''' If SAVE_FILE != exists, start new game. '''

    ''' But for now, just run new_game() '''
    new_game()

### End main(): The initialization phase ###



### Run the game if this file is run as "__main__" ###
if __name__ == "__main__":
    main()
