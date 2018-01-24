import random

from Game.Player import Player
from Game.Bet import Bet

class Bot(Player):
    


    def __init__(self):
        raise Error("Please provide a name")

    def __init__(self, name):
        super(Bot, self).__init__(name)


    def think(self, context):
        raise NotImplementedError("Bot is abstract")


class BotUrchin(Bot):
    def think(self, context):
        return Bet.NOTHING

class BotAllIn(Bot):
    def think(self, context):
        return Bet.ALLIN

class BotBomberman(Bot):
    def think(self, context):
        return random.choice([Bet.BOMB, Bet.TEN])

class BotHonest(Bot):
    def think(self, context):
        return Bet.TEN

class BotRandom(Bot):
    def think(self, context):
        return random.choice([  Bet.TEN,
                                Bet.TEN,
                                Bet.TEN,
                                Bet.NOTHING,
                                Bet.ALLIN])

class BotPareto(Bot):
    def think(self, context):
        return random.choice([  Bet.TEN,
                                Bet.TEN,
                                Bet.TEN,
                                Bet.TEN,
                                Bet.NOTHING])        