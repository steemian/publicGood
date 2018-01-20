from Game import *
from Contrib import *


class Game:
	
	availablePlayers = 	[
		ExamplePlayer,
	]

	availableBots = [
		BotUrchin
	]



	def __init__(self):
		self.players  = []
		for i in range(0, Const.INSTANCES_PER_PLAYER):
			for p in self.availablePlayers:
				self.players.append(p(""))

		self.league = League(self.players)



	def runGame(self):
		for phaseIndex in range(0, Const.PHASES_PER_GAME):
			self.runPhase(phaseIndex)


	def runPhase(self, phaseIndex):
		print ("\n\n\n--PHASE {}".format(phaseIndex))
		self.league.makeTables(phaseIndex)

		for roundIndex in range(0, Const.ROUNDS_PER_PHASE):
			self.runRound(phaseIndex, roundIndex)


	def runRound(self, phaseIndex, roundIndex):
		#print ("\n     ROUND {}.{}".format(phaseIndex, roundIndex))
		self.league.playRound(roundIndex)			


