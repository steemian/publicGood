from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet
from Game.Const import Const

class RiskyPlayer(Player):

    '''
        https://gist.github.com/anonymous/9b0e9abfef4a2551d8df47cc886cd982
    '''

    def getSteemUser(self):
        return "@grungealpha"


    def think(self, context):
        self.lastMove = self.thinkDetails(context)
        return self.lastMove


    def thinkDetails(self, context):

        # First round: go all in if I'm poor
        if (context.roundIndex == 0):
            if (context.playerContexts[self.id].wealth < 70):
                return Bet.ALLIN
            else:
                return Bet.TEN

        # Last round: Be a rat, nobody will remember it
        if (context.roundIndex == Const.ROUNDS_PER_PHASE - 1):
            return Bet.NOTHING

        # Other rounds: were they generous last turn?
        nbZeros = sum(c.previousMoves[context.roundIndex-1] == Bet.NOTHING for c in context.playerContexts.values())
        nbTens = sum(c.previousMoves[context.roundIndex-1] == Bet.TEN for c in context.playerContexts.values())
        nbAllIn = sum(c.previousMoves[context.roundIndex-1] == Bet.ALLIN for c in context.playerContexts.values())

        if (self.lastMove == Bet.NOTHING):
            nbZeros -= 1
        if (self.lastMove == Bet.TEN):
            nbTens -= 1
        if (self.lastMove == Bet.ALLIN):
            nbAllIn -= 1


        # Actual decision
        if (nbZeros > 4):
            return Bet.NOTHING

        if (nbAllIn > 0):
            return Bet.ALLIN

        return Bet.TEN
