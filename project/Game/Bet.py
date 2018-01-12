from enum import Enum

class Bet(Enum):
	UNDECIDED = 0
	TEN = 1
	BOMB = 2
	NOTHING = 3
	ALLIN = 4


	def desc(self, arg):
		print (arg + "youyou")