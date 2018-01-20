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

		shuffle(self.humans)
		self.tables = []

		humansIndex = 0
		minHumansPerTable = floor(totalHumans / nbTables)

		for tabIndex in range(0,nbTables):

			if ((totalHumans-humansIndex)/(nbTables-tabIndex) > minHumansPerTable):
				curHumans = minHumansPerTable+1
			else:
				curHumans = minHumansPerTable

			humansToAdd = self.humans[humansIndex:humansIndex+curHumans]
			#TODO: add bots, count them and remove the -1 below
			table = Table(humansToAdd, "Tab {}".format(tabIndex), tabIndex, -1, totalHumans)
			self.tables.append(table)
			humansIndex += curHumans

