from Game.Player import Player
from Game.Bet import Bet

class Bot(Player):
	

	def __init__(self, name):
		self.name = "[{} ({})]".format(name, type(self).__name__)

	def decide(self, context):
		raise NotImplementedError("Bot is abstract")



class BotUrchin(Bot):
	def decide(self, context):
		return Bet.NOTHING

class BotAllIn(Bot):
	def decide(self, context):
		return Bet.ALLIN

class BotBomberman(Bot):
	def decide(self, context):
		return Bet.BOMB

class BotHonest(Bot):
	def decide(self, context):
		return Bet.TEN

class BotRandom(Bot):
	def decide(self, context):
		raise NotImplementedError