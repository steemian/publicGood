from enum import Enum

class Bet(Enum):
	NOTHING = 0
	ALLIN = 1
	TEN = 2
	BOMB = 3

	def desc(self, arg):
		print (arg + "youyou")