from Game.Bet import Bet

class Table:
	
	pot = 0
	bombs = 0

	def __init__(self, players):
		self.players = players

	def play(self):
		for p in self.players:
			
			p.bet(0)

			#print ("{} decision={} play={}".format(p.name, p.decision, p.play))
			
			if (p.play == Bet.TEN):
				if (p.ownings >= 10):
					p.ownings -= 10
					self.pot += 10
				else:
					print ("Player owns {}. Fallback to AllIn"
						.format(p.ownings))
					p.play = ALLIN
			if (p.play ==Bet.BOMB):
				if (p.bombs >= 1):
					p.bombs -= 1
					self.bombs += 1
				else:
					p.play = NOTHING
			if (p.play == Bet.ALLIN):
				self.pot += p.ownings
				p.ownings = 0
			if (p.play == Bet.NOTHING):
				pass
			if (p.play == Bet.UNDECIDED):
				print ("   UNDECIDED")


			print ("{} bets {}-{} -> pot {}{} Left {}{}".format(
					p.name, 
					p.decision.name,
					p.play.name, 
					'*' * self.bombs, 
					self.pot,
					'*' * p.bombs, 
					p.ownings))

	def distribute(self):
		for p in self.players:
			print ("distributing to {}".format(p))
			p.ownings += 2*self.pot/len(players)
			if (bombs >= 0 and p.curBet == NOTHING):
				players.remove(p)


	