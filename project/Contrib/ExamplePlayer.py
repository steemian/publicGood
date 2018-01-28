from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ExamplePlayer(Player):


    def getSteemUser(self):
        return "@gbd"



    def think(self, context):


        # First round bet a regular ten
        if (context.roundIndex == 0):
            return Bet.TEN


        # Subsequent rounds: bet ten unless the table had a majority of urchins (watching last turn only)
        nbUrchins = sum(c.previousMoves[context.roundIndex-1] == Bet.NOTHING for c in context.playerContexts.values())
        nbPlayers = len(context.playerContexts.values())
        if (nbUrchins > 2):
            return Bet.NOTHING
        else:
            return Bet.TEN
