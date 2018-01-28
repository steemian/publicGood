from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet
from Game.Const import Const

class SocialPlayer(Player):

    '''
        https://gist.github.com/anonymous/c575d9023d56cd1d45abe7eacf2421d7
    '''

    def getSteemUser(self):
        return "@grungealpha"

    signature = [   
            Bet.NOTHING,
            Bet.TEN,
            Bet.TEN,
            Bet.NOTHING,
            Bet.TEN,
        ]



    def friendlyMove(self, context, friends, roundIndex):
        if (len(friends) > 4):  # Nearly impossible, but worth trying
            print ("Social {} found optimal !!!".format(self.id))
            return Bet.ALLIN

        if (len(friends) > 2):
            if (self.id == self.bestInLine(friends)):
                print ("Social {} feels best in line of {}".format(self.id, len(friends)))
                return Bet.NOTHING
            else: 
                return Bet.ALLIN

        # if not enough friends found, play it safe
        return Bet.NOTHING



    def isFriend(self, playerContext, roundIndex):

        if (playerContext.previousMoves[0:len(self.signature)] != self.signature):
            return False
        return True




    def bestInLine(self, players):

        best = players[0]

        for p in players:
            if (p.wealth > best.wealth):
                best = p
            if (p.wealth == best.wealth and p.id < best.id):
                best = p

        return best.id



    def think(self, context):

        # First few rounds: play signature so that friends will idenify me
        if (context.roundIndex < len(self.signature)):
            return self.signature[context.roundIndex]

        # then count friends and coordinate if it's worth it
        friends = list(filter(lambda p:self.isFriend(p, context.roundIndex), context.playerContexts.values()))

        move = self.friendlyMove(context, friends, context.roundIndex)

        return move

