from Game.Bet import Bet

class Player:
	
	ownings = 100
	bombs = 1
	action = Bet.UNDECIDED
	decision = Bet.UNDECIDED

	def __init__(self, name):
		self.name = name


	def think(self, context):
		raise NotImplementedError("Player is abstract")


	def decide(self, context):
		#context = 0
		self.decision = self.think(context)
		self.action = self.decision
		#print ("{} decided {}".format(self.name, self.decision))
		return self.decision

	