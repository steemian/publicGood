from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ExamplePlayer(Player):
	def think(self, context):

		print (context.describe())

		return Bet.ALLIN