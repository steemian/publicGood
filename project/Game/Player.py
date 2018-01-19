import random, string

from Game.Bet import Bet
from Game.Const import Const


class Player:
	
	ownings = 100
	bombs = 1
	action = Bet.UNDECIDED
	decision = Bet.UNDECIDED
	id = 0

	def __init__(self, name):
		choices = string.ascii_uppercase + string.digits
		self.id = ''.join(random.choices(choices, k=Const.RANDOM_ID_LEN))
		self.name = "[{} {} ({})]".format(name, self.id, type(self).__name__)


	def think(self, context):
		raise NotImplementedError("Player is abstract")


	def decide(self, context):
		#context = 0
		self.decision = self.think(context)
		self.action = self.decision
		print ("{} decided {}".format(self.name, self.decision))
		return self.decision

	
