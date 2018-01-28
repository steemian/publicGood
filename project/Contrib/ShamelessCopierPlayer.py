from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet
from Game.Const import Const

class ShamelessCopierPlayer(Player):

    '''
        coded from the spec given in the article body: https://steemit.com/aicontest/@gbd/the-ai-contest-1-non-programmers-welcome
    '''

    def getSteemUser(self):
        return "@gbd"


    def think(self, context):

        if (context.roundIndex == 0):
            return Bet.TEN

        richest = max(context.playerContexts.values(), key=lambda pc: pc.wealth)
        return richest.previousMoves[-1]

