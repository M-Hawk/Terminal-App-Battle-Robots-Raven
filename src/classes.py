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
    def __init__(self, player_one, player_two):
        # self.p2 = ComputerPlayer()
        ""
    # Method that clears the terminal throughout the game so players don't have to scroll
    def clear_terminal():
        system("cls" if name == "nt" else "clear")

    # Game mode select method
    def game_mode(self):
        Game.clear_terminal()
        options = ["Single Player", "Multi Player", "Exit Game"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        while menu_entry_index != 2:
            if options[menu_entry_index]
        # if self.game = single_player_mode()
        # self.game = multi_player_mode()

    def single_player_mode(self):
        pass


    def multi_player_mode(self):
        pass

    # def 


# MAINNNN HERE



player_one = Player("Jax")
player_two = ComputerPlayer()

# print(player1.get_name())
# print(bot1.get_name())
# print(bot1.get_health())


game = Game(player_one, player_two)
game.game_mode()