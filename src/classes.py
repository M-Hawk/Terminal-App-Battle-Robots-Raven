from random import choice
from os import system, name
from time import sleep

# Player Class for inidividual human players

class Player():
    def __init__(self, name, health = 200):
        self.__name = name
        self.__health = health

    def get_name(self):
       return self.__name

    def get_health(self):
       return self.__health

    def set_name(self, name):
        self.__name = name

# Child Class of the Player Class for AI specifics

class ComputerPlayer(Player):

    # Random names for AI player
    bot_names = ["Terminator", "Annihilator", "Destroyer", "Crusher", "Nuts-n-Bolts", "Link",
    "Mechanicus", "Ripper", "Tank", "Shredder"]
    # Added private variable name here to prevent potential access to this random name variable
    __rand_name = choice(bot_names)

    def __init__(self, name = __rand_name):
        self.__name = name
        super().__init__(self)

    # FIND A BETTER WAY THAN REPEATING CODE TO USE GETTERS SETTERS
    def get_name(self):
       return self.__name

    def get_health(self):
       return self.__health

    def set_name(self, name):
        self.__name = name


class Game():

    def __init__(self):
        ""

    def clear_terminal(self):
        system("cls" if name == "nt" else "clear")

    def game_mode(self):
        options = ["Single Player", "Multi Player", "Exit Game"]
        for index, item in enumerate(options):
            print(f"\n{index+1}) {item}\n")
        self.game_type = input("What game mode would you like to play? ")
        self.game_type.capitilize()
        if self.gametype == 






# MAINNNN HERE

game = Game()
game.game_mode()

# player1 = Player("Jax")
# bot1 = ComputerPlayer()

# print(player1.get_name())
# print(bot1.get_name())