import random

from Game import *



def smokeTest():
	players = [] 
	for i in range(0,3):
		players.append(BotAllIn(i))
	t = Table(players)
	t.play()

def populateTable():
	players = [] 
	
	#print (repr(Bet.ALLIN))
	#Bet.ALLIN.desc("DDD")


	for i in range(0, 5):
		players.append(BotAllIn("P" + str(i)))

	players.append(BotBomberman("P" + str(5)))
	players.append(BotHonest("P" + str(6)))

	for i in range(7, 10):		
		players.append(BotUrchin("P" + str(i)))

	t = Table(players)
	t.play()
	t.distribute()







# Run tests

print ("\n------  smokeTest")
smokeTest()
print ("\n------  populateTable")
populateTable()