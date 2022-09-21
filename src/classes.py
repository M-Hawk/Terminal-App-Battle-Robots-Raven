from random import choice
from os import system, name
from time import sleep
from simple_term_menu import TerminalMenu

# Player Class for inidividual human players

class Player():
    def __init__(self, name, health = 200, body_movement = "undefined", arm_weapon = "undefined"):
        self.__name = name
        self.__health = health
        self.__body_movement = body_movement
        self.__arm_weapon = arm_weapon

    def get_name(self):
       return self.__name

    def get_health(self):
       return self.__health

    def set_name(self, name):
        self.__name = name

    def set_body_movement(self, body_movement):
        self.__body_movement = body_movement

    def set_arm_weapon(self, arm_weapon):
        self.__arm_weapon = arm_weapon


# Child Class of the Player Class for AI specifics

class ComputerPlayer(Player):

    # Random names for AI player
    bot_names = ["Terminator", "Annihilator", "Destroyer", "Crusher", "Nuts-n-Bolts", "Link",
    "Mechanicus", "Ripper", "Tank", "Shredder"]
    # Added private variable name here to prevent potential access to this random name variable

    def __init__(self):
        self.__name = choice(ComputerPlayer.bot_names)
        super().__init__(self.__name)





class Game():

    # Method that clears the terminal throughout the game so players don't have to scroll

    def clear_terminal():
        system("cls" if name == "nt" else "clear")

    def game_mode():
        options = ["Single Player", "Multi Player", "Exit Game"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        while menu_entry_index != 2:
            if menu_entry_index == 0:
                single_player_mode()
            elif menu_entry_index == 1:
                pass
                # self.multi_player_mode()
            menu_entry_index = terminal_menu.show()


    def battle(self, player_one):
        pass

    def single_player_mode(self):
        player_one_name = input("What's you're Battle Robots Name ? ")
        player_one = Player(player_one_name)
        print(f"Welcome, {player_one.get_name()}")
        player_two = ComputerPlayer()
        print(f"You're Battling! {player_two.get_name()}")
        print(player_two.get_name())

    # Game mode select method




# MAINNNN HERE



# player_one = Player("Jax")
# player_two = ComputerPlayer()

# print(player1.get_name())
# print(bot1.get_name())
# print(bot1.get_health())

player_one = Player("Jax")

Game.game_mode()

