from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet
from Game.Const import Const

class ExGiver(Player):


	def think(self, context):
		return Bet.TEN


