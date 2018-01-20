import random

from Game import *
from Contrib import *



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

		dispatched = l.totalPlayersInTables()
		if (len(l.humans) != dispatched):
			print("")
			print("")
			print("   ERROR  {} != {}  ".format(len(l.humans), dispatched))
			print("")
			print("")

def fullGame():

	players = []

	for i in range(0, Const.INSTANCES_PER_PLAYER):
		players.append(BotRandom("R{}".format(i)))
		players.append(ExamplePlayer("X{}".format(i)))
		players.append(BotHonest("H{}".format(i)))
		players.append(BotUrchin("H{}".format(i)))
		players.append(BotUrchin("H{}".format(i)))

	l = League(players)


	for phaseIndex in range(0, Const.PHASES_PER_GAME):
		print ("\n\n\n--PHASE {}".format(phaseIndex))
		l.makeTables(phaseIndex)

		for roundIndex in range(0, Const.ROUNDS_PER_PHASE):
			print ("\n     ROUND {}.{}".format(phaseIndex, roundIndex))
			l.playRound(roundIndex)



def instantiateGame():

	g = Game()
	g.runGame()




# Run tests

#smokeTest()
#populateTable()
#tablesDispatch()
#fullGame()
instantiateGame()
