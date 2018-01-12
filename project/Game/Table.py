class Table:
	

	def __init__(self, players):
		self.players = players

	def play(self):
		for p in self.players:
			bet = p.bet()
			print ("{} bets {}".format(p.name, repr(bet)))

	