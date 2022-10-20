import math
import random

class Player:
    def _init_(self, letter):
        # letter is X or O 
        self.letter = letter

        # we want all players to be able to get their next move given a game 
    def get_move(self, game): 
        pass

class RandomComputerPlayer(Player): 
    def _init_(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())

class HumanPlayer(Player):
    def _init_(self, letter):
         super()._init_(letter)

    def get_move(self, game):
        valid    



