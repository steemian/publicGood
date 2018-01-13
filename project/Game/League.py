from random import shuffle 
from math import ceil, floor

from Game.Player import Player
from Game.Table import Table
from Game.Const import Const 	

class League:

	tables = []

	def __init__(self, humans):
		self.humans = humans

	def totalPlayersInTables(self):
		toreturn = 0
		for t in self.tables:
			toreturn += len(t.players)
		return toreturn

	def makeTables(self):
		
		nbHumans = len(self.humans)
		nbTables = ceil(nbHumans / Const.MAX_HUMANS_PER_TABLE)
		nbHumansPerTable = nbHumans / nbTables
		print ("Dispatch {} humans into {} tables: {} each"
			.format(nbHumans, nbTables, nbHumansPerTable))

		shuffle(self.humans)
		self.tables = []
		start = 0.

		for tabIndex in range(0,nbTables):
			end = start + nbHumansPerTable
			table = Table(self.humans[round(start):ceil(end)])
			self.tables.append(table)

			print ("Table {:2} has {:2} players from {:2.1f} to {:2.1f}"
				.format(tabIndex, len(table.players), start, end))
			start += len(table.players)

