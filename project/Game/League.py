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
		
		totalHumans = len(self.humans)
		nbTables = ceil(totalHumans / Const.MAX_HUMANS_PER_TABLE)


		#nbHumansPerTable = totalHumans / nbTables
		print ("\nDispatch {} humans into {} tables: {:2.1f} each".format(totalHumans, nbTables, totalHumans / nbTables))

		shuffle(self.humans)
		self.tables = []
		start = 0.
		popMin = 9999
		popMax = 0

		humansIndex = 0


		minHumansPerTable = floor(totalHumans / nbTables)


		for tabIndex in range(0,nbTables):

			if ((totalHumans-humansIndex)/(nbTables-tabIndex) > minHumansPerTable):
				curHumans = minHumansPerTable+1
			else:
				curHumans = minHumansPerTable

#			print ("{} humans for {} tables left (avg {:2.1f}) - choose {}".format(
#					(totalHumans-humansIndex),
#					(nbTables-tabIndex),
#					(totalHumans-humansIndex)/(nbTables-tabIndex),
#					curHumans
#				))	

			humansToAdd = self.humans[humansIndex:humansIndex+curHumans]
			table = Table(humansToAdd, "Tab {}".format(tabIndex), tabIndex, -1, totalHumans)
			self.tables.append(table)
			humansIndex += curHumans

#			print ("Table {:2} has {:2} players from {:2.1f} to {:2.1f}"
#				.format(tabIndex, len(table.players), start, end))

			#print("cur={} min={} max={}".format(len(table.players),popMin, popMax))
			popMin = min(popMin, len(table.players))
			popMax = max(popMax, len(table.players))
			#print("cur={} min={} max={}\n\n".format(len(table.players),popMin, popMax))



		if (popMax-popMin > 1)	:
			print ("{:3} humans in {:2} tables (avg={:2.2f}). Min={} Max={}  Delta={}"
				.format(totalHumans, len(self.tables), (totalHumans-humansIndex)/(nbTables-tabIndex), popMin, popMax, popMax-popMin))