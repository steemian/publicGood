from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet
from Game.Const import Const

class AveragePlayer(Player):

    '''
        compute a weighted average of all previous moves, and do the opposite
    '''

    RoundWeights = [10, 9, 5, 2, 1, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    BetWeights = {Bet.TEN: 10,  Bet.NOTHING: 10, Bet.ALLIN : 10}

    def getSteemUser(self):
        return "@grungealpha"


    def think(self, context):

        if (context.roundIndex < 1):
            return Bet.NOTHING

        avg = {Bet.TEN: 0,  Bet.NOTHING: 0, Bet.ALLIN : 0}

        for i in range(0, context.roundIndex):
            for p in context.playerContexts.values():
                if (p.id == self.id):
                    next
                print ("id={}  i={}".format(p.id, i))
                avg[p.previousMoves[i]] += self.BetWeights[p.previousMoves[i]] * self.RoundWeights[context.roundIndex - i -1]

        if (avg[Bet.TEN] > avg[Bet.NOTHING]):
            return Bet.TEN
        else:
            return Bet.NOTHING

