from Game import Table, Player
from Game import Bot, BotAllIn, BotUrchin
import random


def smokeTest():
	players = [] 
	for i in range(0,3):
		players.append(Player(i))
	t = Table(players)
	t.play()

def populateTable():
	players = [] 
	
	for i in range(0, 5):
		players.append(BotAllIn("P" + str(i)))

	for i in range(5, 10):		
		players.append(BotUrchin("P" + str(i)))

	t = Table(players)
	t.play()







# Run tests

print ("\n------  smokeTest")
smokeTest()
print ("\n------  populateTable")
populateTable()