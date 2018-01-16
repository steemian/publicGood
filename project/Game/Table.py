import copy

from Game.Bet import Bet

class Table:
	
	pot = 0
	bombs = 0

	def __init__(self, players, name):
		self.players = players
		self.name = name

	def play(self, roundIndex):
		
		self.pot = 0
		self.bombs = 0
		self.context.roundIndex = roundIndex 

		for p in self.players:

			contextCopy = copy.deepcopy(self.context)
			p.decide(contextCopy)

			if (p.action == Bet.TEN):
				if (p.ownings >= 10):
					p.ownings -= 10
					self.pot += 10
				else:
					print ("Player owns {}. Fallback to AllIn"
						.format(p.ownings))
					p.action = Bet.ALLIN

			if (p.action ==Bet.BOMB):
				if (p.bombs >= 1):
					p.bombs -= 1
					self.bombs += 1
				else:
					p.action = Bet.NOTHING

			if (p.action == Bet.ALLIN):
				self.pot += p.ownings
				p.ownings = 0
			if (p.action == Bet.NOTHING):
				pass
			if (p.action == Bet.UNDECIDED):
				print ("   UNDECIDED")


	def distribute(self):
		payout = 2*self.pot/(len(self.players)+1)
		print ("PAYOUT  2x {}{:3.2f} / {:2} = {:3.2f} ".format(
							'*' * self.bombs, self.pot, len(self.players)+1, payout))

		for p in list(self.players):
			p.ownings += payout
			
			# If you forgot you had no bomb left, you may die from other bombers. Sad story.
			if (self.bombs > 0 and p.action == Bet.NOTHING):
				self.players.remove(p)
				

#			print ("{:20} bets {:>9}-{:9} - {}{:3.2f} -> {}{:3.2f}  {}".format(
#					p.name, 
#					p.decision.name,
#					p.action.name, 
#					'*' * p.bombs, 
#					p.ownings-payout,
#					'*' * p.bombs, 
#					p.ownings,
#					"**BOOM**" * (self.bombs > 0 and p.action == Bet.NOTHING) ))		



	