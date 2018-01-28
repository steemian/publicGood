from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class GrimTriggerPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.prev_wealth = None
        self.bet = True

    def getSteemUser(self):
        return "@scorpil"

    def think(self, context):
        if self.prev_wealth == None:
            return self.send(Bet.TEN)

        if self.bet and self.prev_wealth <= self.wealth - 10:
            return self.send(Bet.TEN)

        self.bet = False
        return self.send(Bet.NOTHING)

    def send(self, bet):
        self.prev_wealth = self.wealth
        return bet