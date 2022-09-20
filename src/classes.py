from random import choice


# Player class for inidividual human players

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


    # def bot_name():
        
        
    #     return random_name








bot1 = ComputerPlayer()

print(bot1.get_name())