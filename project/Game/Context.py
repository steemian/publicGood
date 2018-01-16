from Game.Player import Player
from Game.Table import Table




class PlayerContext:

	wealth = 0;
	previousMoves = []


class Context:

	players = []
	roundIndex = 0		# out of Const.ROUNDS_PER_PHASE
	phaseIndex = 0		# out of PHASES_PER_GAME

	def describe(self):
		description =  "           || CONTEXT -----------------||\n"  
		description += "              ROUND {}.{}\n".format(self.phaseIndex, self.roundIndex)

		for p in self.players:
			description += "           {:15} ({}$) - played {}".format(
				p.name,
				p.wealth,
				p.previousMoves)

		description += "\n           ||-----------------------------"

		return description
				
