import random, string

from Game.Bet import Bet
from Game.Const import Const


class Player:
	
	def __init__(self, name):
		self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Const.RANDOM_ID_LEN))
		self.wealth = Const.STARTING_WEALTH
		self.action = Bet.UNDECIDED
		self.decision = Bet.UNDECIDED
		self.name = "[{} {} ({})]".format(name, self.id, type(self).__name__)


	def think(self, context):
		raise NotImplementedError("Player is abstract")


	def decide(self, context):
		self.decision = self.think(context)
		self.action = self.decision
		return self.decision

	
