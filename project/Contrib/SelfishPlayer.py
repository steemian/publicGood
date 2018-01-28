from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class SelfishPlayer(Player):

    def getSteemUser(self):
        return "@amosbastian"
    
    # Doesn't care about context, only himself
    def think(self, context):
        return Bet.NOTHING