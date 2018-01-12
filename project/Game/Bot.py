from Game.Player import Player
from Game.Bet import Bet

class Bot(Player):
	

	def __init__(self, name):
		self.name = "[{} ({})]".format(name, type(self).__name__)

	def bet(self):
		raise NotImplementedError("Bot is abstract")



class BotUrchin(Bot):
	def bet(self):
		return Bet.NOTHING

class BotAllIn(Bot):
	def bet(self):
		return Bet.ALLIN

class BotBomberman(Bot):
	def bet(self):
		return Bet.BOMB

class BotHonest(Bot):
	def bet(self):
		return Bet.TEN


class BotRandom(Bot):
	def bet(self):
		raise NotImplementedError