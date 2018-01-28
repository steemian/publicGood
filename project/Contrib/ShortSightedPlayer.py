from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ShortSightedPlayer(Player):
    '''
        https://gist.github.com/anonymous/0f4ff122deeea6eba1919aef0c2feeab
    '''

    def getSteemUser(self):
        return "@grungealpha"


    def think(self, context):

        # First round bet a regular ten
        if (context.roundIndex == 0):
            return Bet.TEN

        # Subsequent rounds: bet ten unless the table had a lot of zeros (watching last turn only)
        nbZeros = sum(c.previousMoves[context.roundIndex-1] == Bet.NOTHING for c in context.playerContexts.values())
        nbPlayers = len(context.playerContexts.values())
        if (nbZeros > nbPlayers*0.2):
            return Bet.NOTHING
        else:
            return Bet.TEN


        return Bet.ALLIN
