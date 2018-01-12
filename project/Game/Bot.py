from Game import Player

class Bot(Player):
	

	def __init__(self, name):
		self.name = "[{} (BOT)]"

	def bet(self):
		raise NotImplementedError("Bot is abstract")


class BotUrchin(Bot):
	def bet(self):
		return "NOTHING"	


class BotAllIn(Bot):
	def bet(self):
		return "All in"			