from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ConservativePlayer(Player):

  def getSteemUser(self):
    return "@gbd"

  def think(self, context):
    self.lastMove = self.thinkDetails(context)
    return self.lastMove


  def thinkDetails(self, context):
    # First round: TEN
    if (context.roundIndex == 0):
        return Bet.TEN

    # Other rounds: were they generous last turn?
    nbUrchins = sum(c.previousMoves[context.roundIndex-1] == Bet.NOTHING for c in context.playerContexts.values())

    if (self.lastMove == Bet.NOTHING or nbUrchins > 6):
      return Bet.NOTHING

    return Bet.TEN