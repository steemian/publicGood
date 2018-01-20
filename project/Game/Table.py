import copy

from Game.Bet import Bet
from Game.Context import Context, PlayerContext

class Table:
	
#	pot = 0
#	bombs = 0

	def __init__(self, players, name, tableIndex, totalBots, totalHumans):
		self.players = players
		self.name = name
		self.context = Context(players, tableIndex, totalBots, totalHumans)
		self.pot = 0
		self.bombs = 0



	def play(self, phaseIndex, roundIndex):
		
		self.pot = 0
		self.bombs = 0

		self.context.roundIndex = roundIndex 
		self.context.phaseIndex = phaseIndex 

		for p in self.players:

			contextCopy = copy.deepcopy(self.context)
			p.decide(contextCopy)

			if (p.action == Bet.TEN):
				if (p.wealth >= 10):
					p.wealth -= 10
					self.pot += 10
				else:
					print ("Player owns {}. Fallback to AllIn"
						.format(p.wealth))
					p.action = Bet.ALLIN

			if (p.action ==Bet.BOMB):
				if (p.bombs >= 1):
					p.bombs -= 1
					self.bombs += 1
				else:
					p.action = Bet.NOTHING

			if (p.action == Bet.ALLIN):
				self.pot += p.wealth
				p.wealth = 0
			if (p.action == Bet.UNDECIDED):
				raise Error("Undecided bet not allowed at playing time")
			if (p.action == Bet.NOTHING):
				pass


	def distribute(self):
		payout = 2*self.pot/(len(self.players))

#		print ("PAYOUT  2x {}{:>3.2f} / {:2} = {:3.2f} ".format(
#							'*' * self.bombs, self.pot, len(self.players)+1, payout))

		for p in list(self.players):
			p.wealth += payout
			
			# If you forgot you had no bomb left, you may die from other bombers. Sad story.
			if (self.bombs > 0 and p.action == Bet.NOTHING):
				self.players.remove(p)


#			print ("{:25} bets {:>9}-{:9} - {}{:3.2f} -> {}{:3.2f}  {}".format(
#					p.name, 
#					p.decision.name,
#					p.action.name, 
#					'*' * p.bombs, 
#					p.wealth-payout,
#					'*' * p.bombs, 
#					p.wealth,
#					"**BOOM**" * (self.bombs > 0 and p.action == Bet.NOTHING) ))		

		self.context.update(self.players, payout)

				


	