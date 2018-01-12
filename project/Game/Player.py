from Game.Bet import Bet

class Player:
	
	ownings = 100
	bombs = 1

	def __init__(self, name):
		self.name = name
		print ("mk PLAYER -> {}".format(self))



	def bet(self):
		raise NotImplementedError("Player is abstract")

	