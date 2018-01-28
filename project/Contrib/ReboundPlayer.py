from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ReboundPlayer(Player):

    '''
        Bet ten if and only if there was no money at all given last round
    '''

    def getSteemUser(self):
        return "miripiri"



    def think(self, context):

        if (context.roundIndex == 0):
            return Bet.NOTHING


        for player in context.playerContexts.values():
            if (player.previousMoves[-1] != Bet.NOTHING):
                return Bet.NOTHING


        return Bet.TEN
