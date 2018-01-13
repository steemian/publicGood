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
	players.append(BotRandom("P" + str(i)))
	i = i+1
	players.append(BotRandom("P" + str(i)))
	i = i+1

	t = Table(players)

	t.play()
	t.distribute()
	print("")
	t.play()
	t.distribute()

def fullTablePlay():
	players = [] 
	for i in range(0,20):
		c = random.choice([
						BotRandom, 
						BotAllIn, 
						BotHonest, 
						BotBomberman, 
						BotUrchin])
		players.append(c("P{}".format(i)))

	t = Table(players)

	for round in range(0,50):
		if (len(t.players) < 2):
			break

		t.play()
		print("")
		t.distribute()
		print("")
		print("")

	print ("end at round {}".format(round))

def tablesDispatch():

	for n in range(1,40):
		players = [] 
		for i in range(0,n):
			c = random.choice([BotRandom])
			players.append(c("P{}".format(i)))

		l = League(players)
		l.makeTables()





# Run tests

#smokeTest()
#populateTable()

tablesDispatch()