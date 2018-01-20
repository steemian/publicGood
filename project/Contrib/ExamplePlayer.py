from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ExamplePlayer(Player):


	def think(self, context):


		# First round bet a regular ten
		if (context.roundIndex == 0):
			print ("  (AI) : First round")
			return Bet.TEN

		#print (context.describe())

		# Subsequent rounds: bet ten unless the table had a majority of urchins (watching last turn only)
		nbUrchins = sum(c.previousMoves[context.roundIndex-1] == Bet.NOTHING for c in context.playerContexts.values())
		nbPlayers = len(context.playerContexts.values())
		print ("  (AI) : Urchins last round: {}/{}".format(nbUrchins, nbPlayers))
		if (nbUrchins > nbPlayers*0.03):
			return Bet.NOTHING
		else:
			return Bet.TEN


		return Bet.ALLIN