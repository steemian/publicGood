from enum import Enum

from Game.Player import Player
from Game.Bet import Bet




class PlayerContext:

#	wealth = 0;
#	previousMoves = []
#	id = ""
#	player = ""

	def __init__(self, player):
		self.wealth = player.wealth
		self.id = player.id
		self.player = player 		#TODO: remove this: code should not know it
		self.previousMoves = []


class Context:

#	playerContexts = {}
#   payouts = []
#	roundIndex = 0		# out of Const.ROUNDS_PER_PHASE
#	phaseIndex = 0		# out of PHASES_PER_GAME
#	totalHumans = 0
# 	totalBots = 0
#	tableIndex = 0

	def __init__(self, players, tableIndex, totalBots, totalHumans):
		self.payouts = []
		self.playerContexts = {}
		self.roundIndex = 0
		self.phaseIndex = 0
		self.tableIndex = tableIndex
		self.totalBots = totalBots
		self.totalHumans = totalHumans
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

		lastPayout = "{:3.2f}".format(self.payouts[-1]) if (len(self.payouts) > 0) else "N/A"

		description = "  TABLE {:2}  ROUND {}.{}  - pays {} each - Hum/Bots = {:2}/{:2}\n".format(
				self.tableIndex, 
				self.phaseIndex, 
				self.roundIndex, 
				lastPayout, 
				self.totalHumans, 
				self.totalBots)

		for p in self.playerContexts.values():
			description += "     {:6} ({:15})   {:<4.2f} \t-  [{}];\n".format(
				p.id,
				type(p.player).__name__,		#TODO: remove this: code should not know it
				p.wealth,
				" ".join(m.asChar() for m in p.previousMoves)
				)

		return description


				
