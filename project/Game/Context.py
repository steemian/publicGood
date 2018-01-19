from Game.Player import Player
#from Game.Table import Table




class PlayerContext:

	wealth = 0;
	previousMoves = []
	id = ""

	def __init__(self, player):
		self.wealth = player.wealth
		self.id = player.id


class Context:

	playerContexts = {}
	roundIndex = 0		# out of Const.ROUNDS_PER_PHASE
	phaseIndex = 0		# out of PHASES_PER_GAME


	def __init__(self, players):
		for p in players:
			self.playerContexts[p.id] = PlayerContext(p)


	def update(self, players):
		print ("     CONTEXT UPDATE\n{}".format(players))

		print ("     CONTEXT BEFORE\n{}".format(self.describe()))

		for p in players:	
			print ("           P {} - {}".format(p.id, self.playerContexts[p.id].id))
			self.playerContexts[p.id].previousMoves.append(p.action)
			self.playerContexts[p.id].wealth = p.wealth
		print ("     CONTEXT AFTER\n{}".format(self.describe()))


	def describe(self):
		description =  "           || CONTEXT -----------------||\n"  
		description += "              ROUND {}.{}\n".format(self.phaseIndex, self.roundIndex)


		for p in self.playerContexts.values():
			description += "           {:15} ({}$) - played [{}];\n".format(
				p.id,
				p.wealth,
				" ".join(str(m.name) for m in p.previousMoves))

		description += "\n           ||-----------------------------"

		return description
				
