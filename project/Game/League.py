from random import shuffle 
from math import ceil

from Game.Player import Player
from Game.Table import Table
from Game.Const import Const 	

class League:

	def __init__(self, humans):
		self.humans = humans

	def makeTables(self):
		
		shuffle(self.humans)
		nbHumans = len(self.humans)
		nbHumansPerTable = 0
	nbTables = ceil(nbHumans / Const.MAX_HUMANS_PER_TABLE)
		nbHumansPerTable = nbHumans / nbTables
		print ("Dispatch {} humans into {} tables: {} each"
			.format(nbHumans, nbTables, nbHumansPerTable))


