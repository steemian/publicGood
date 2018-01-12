import random

from Game.Player import Player
from Game.Bet import Bet

class Bot(Player):
	

	def __init__(self, name):
		self.name = "[{} ({})]".format(name, type(self).__name__)

	def think(self, context):
		raise NotImplementedError("Bot is abstract")



class BotUrchin(Bot):
	def think(self, context):
		return Bet.NOTHING

class BotAllIn(Bot):
	def think(self, context):
		return Bet.ALLIN

class BotBomberman(Bot):
	def think(self, context):
		return random.choice([Bet.BOMB, Bet.TEN])

class BotHonest(Bot):
	def think(self, context):
		return Bet.TEN

class BotRandom(Bot):
	def think(self, context):
		raise NotImplementedError