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


	def playRound (self, roundIndex):
		for t in self.tables:
			print ("\n      TABLE {}/{}".format(t.name, "X"))
			t.play(roundIndex)
			t.distribute()



	def makeTables(self, phaseIndex):
		
		nbHumans = len(self.humans)
		nbTables = ceil(nbHumans / Const.MAX_HUMANS_PER_TABLE)
		nbHumansPerTable = nbHumans / nbTables

		shuffle(self.humans)
		self.tables = []
		start = 0.

		for tabIndex in range(0,nbTables):
			end = start + nbHumansPerTable
			table = Table(self.humans[round(start):ceil(end)], "Tab {}".format(tabIndex))
			table.context = Context(table.players)
			table.context.phaseIndex = phaseIndex
			self.tables.append(table)

			start += len(table.players)

