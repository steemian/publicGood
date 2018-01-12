from Game.Bet import Bet

class Player:
	
	ownings = 100
	bombs = 1
	play = Bet.UNDECIDED
	decision = Bet.UNDECIDED

	def __init__(self, name):
		self.name = name


	def decide(self, context):
		raise NotImplementedError("Player is abstract")

	def bet(self, context):
		self.play = self.decision = self.decide(context)
		#print ("{} decided {}".format(self.name, self.decision))
		return self.decision

	