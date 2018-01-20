from random import shuffle 
from math import ceil, floor

from Game.Player import Player
from Game.Table import Table
from Game.Const import Const 	
from Game.Context import Context, PlayerContext

class League:

	# tables = []

	def __init__(self, humans):
		self.humans = humans
		for h in humans:
			h.wealth = Const.STARTING_WEALTH
			h.bombs = Const.STARTING_BOMBS

	def totalPlayersInTables(self):
		toreturn = 0
		for t in self.tables:
			toreturn += len(t.players)
		return toreturn

		
	def playRound (self, phaseIndex, roundIndex):
		print (" -ROUND {}/{} -------".format(roundIndex, Const.ROUNDS_PER_PHASE))
		for t in self.tables:
			#print ("\n -TABLE {}/{}".format(t.name, "X"))
			t.play(phaseIndex, roundIndex)
			t.distribute()



	def makeTables(self, phaseIndex):
		
		nbHumans = len(self.humans)
		nbTables = ceil(nbHumans / Const.MAX_HUMANS_PER_TABLE)
		nbHumansPerTable = nbHumans / nbTables
		#print ("Dispatch {} humans into {} tables: {} each".format(nbHumans, nbTables, nbHumansPerTable))

		shuffle(self.humans)
		self.tables = []
		start = 0.
		popMin = 9999
		popMax = 0

		for tabIndex in range(0,nbTables):
			end = start + nbHumansPerTable
			table = Table(self.humans[round(start):ceil(end)], "Tab {}".format(tabIndex), tabIndex, -1, nbHumans)
			self.tables.append(table)

#			print ("Table {:2} has {:2} players from {:2.1f} to {:2.1f}"
#				.format(tabIndex, len(table.players), start, end))
			start += len(table.players)

			#print("cur={} min={} max={}".format(len(table.players),popMin, popMax))
			popMin = min(popMin, len(table.players))
			popMax = max(popMax, len(table.players))
			#print("cur={} min={} max={}\n\n".format(len(table.players),popMin, popMax))



		if (popMax-popMin > 1)	:
			print ("{:3} humans in {:2} tables (avg={:2.2f}). Min={} Max={}  Delta={}"
				.format(nbHumans, len(self.tables), nbHumansPerTable, popMin, popMax, popMax-popMin))