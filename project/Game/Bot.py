from Game.Player import Player
from Game.Bet import Bet

class Bot(Player):
	

	def __init__(self, name):
		self.name = "[{} (BOT)]".format(name)

	def bet(self):
		raise NotImplementedError("Bot is abstract")


class BotUrchin(Bot):
	def bet(self):
		return Bet.NOTHING


class BotAllIn(Bot):
	def bet(self):
		return Bet.ALLIN