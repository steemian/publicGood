from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet
from Game.Const import Const

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class SocialPlayer(Player):

    '''
        https://gist.github.com/anonymous/2629bf9599fcc41a6dbf26111e8f9818
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
            return Bet.ALLIN

        if (len(friends) > 2):
            if (self.id == self.bestInLine(friends)):
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

