from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet


class T4TPlayer(Player):
    def __init__(self, name):
        super(T4TPlayer, self).__init__(name)
        self.wealth_before = None

    def getSteemUser(self):
        return "@laxam"

    def think(self, context):
        cooperative = self.wealth_before and self.wealth_before <= self.wealth - 10
        bet = Bet.TEN if cooperative else Bet.NOTHING
        self.wealth_before = self.wealth
        return bet