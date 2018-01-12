from Game.Bet import Bet

class Table:
	
	pot = 0
	bombs = 0

	def __init__(self, players):
		self.players = players

	def play(self):
		for p in self.players:
			bet = p.bet()
			
			if (bet == Bet.TEN):
				if (p.ownings >= 10):
					p.ownings -= 10
					self.pot += 10
				else:
					print ("Player owns {}. Fallback to AllIn"
						.format(p.ownings))
					bet = ALLIN

			if (bet ==Bet.BOMB):
				if (p.bombs >= 1):
					p.bombs -= 1
					self.bombs += 1
				else:
					bet = NOTHING


			if (bet == Bet.ALLIN):
				self.pot += p.ownings
				p.ownings = 0

			if (bet == Bet.NOTHING):
				pass


			print ("{} bets {} -> pot {}{} Left {}{}".format(
					p.name, 
					bet, 
					'*' * self.bombs, 
					self.pot,
					'*' * p.bombs, 
					p.ownings))

	