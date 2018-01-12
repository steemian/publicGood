from Game import Table, Player

players = [] 

for i in range(0,3):
	players.append(Player(i))

t = Table(players)

t.play()