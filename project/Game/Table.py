from Game.Bet import Bet

class Table:
	
	pot = 0
	bombs = 0

	def __init__(self, players):
		self.players = players

	def play(self):
		for p in self.players:

			p.decide()

			if (p.action == Bet.TEN):
				if (p.ownings >= 10):
					p.ownings -= 10
					self.pot += 10
				else:
					print ("Player owns {}. Fallback to AllIn"
						.format(p.ownings))
					p.action = bet.ALLIN

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


			print ("{} bets {}-{} -> pot {}{} Left {}{}".format(
					p.name, 
					p.decision.name,
					p.action.name, 
					'*' * self.bombs, 
					self.pot,
					'*' * p.bombs, 
					p.ownings))

	def distribute(self):
		share = 2*self.pot/len(self.players)
		for p in self.players:
			p.ownings += share
			print ("{} now owns {} ".format(p.name, p.ownings))
			if (self.bombs >= 0 and p.decision == Bet.NOTHING):
				self.players.remove(p)


	