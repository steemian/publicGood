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

	i = 0

	players.append(BotHonest("P" + str(i)))
	i = i+1
	players.append(BotUrchin("P" + str(i)))
	i = i+1
	players.append(BotHonest("P" + str(i)))
	i = i+1
	players.append(BotBomberman("P" + str(i)))
	i = i+1
	players.append(BotBomberman("P" + str(i)))
	i = i+1
	players.append(BotAllIn("P" + str(i)))
	i = i+1
	players.append(BotBomberman("P" + str(i)))
	i = i+1
	players.append(BotHonest("P" + str(i)))
	i = i+1
	players.append(BotUrchin("P" + str(i)))
	i = i+1

	t = Table(players)

	t.play()
	t.distribute()
	print("")
	t.play()
	t.distribute()







# Run tests

print ("\n------  smokeTest")
smokeTest()
print ("\n------  populateTable")
populateTable()