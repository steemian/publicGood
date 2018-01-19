from Game.Player import Player
#from Game.Table import Table




class PlayerContext:

#	wealth = 0;
#	previousMoves = []
#	id = ""
#	player = ""

	def __init__(self, player):
		self.wealth = player.wealth
		self.id = player.id
		self.player = player
		self.previousMoves = []


class Context:

#	playerContexts = {}
#	roundIndex = 0		# out of Const.ROUNDS_PER_PHASE
#	phaseIndex = 0		# out of PHASES_PER_GAME


	def __init__(self, players):
		self.payouts = []
		self.playerContexts = {}
		for p in players:
			self.playerContexts[p.id] = PlayerContext(p)


	def update(self, players, payout):
		self.payouts.append(payout)
		for p in players:	
			c = self.playerContexts[p.id]
			c.previousMoves.append(p.action)
			c.wealth = p.wealth
		print (self.describe())


	def describe(self):

		description = "      ROUND {}.{}  - pays {:3.2f} each\n".format(self.phaseIndex, self.roundIndex, self.payouts[-1])
		for p in self.playerContexts.values():
			description += "        {:6} ({:15})     ({:<3.2f} $)\t- played [{}];\n".format(
				p.id,
				type(p.player).__name__,
				p.wealth,
				" ".join(str(m.name) for m in p.previousMoves))

		return description
				
