import random
import datetime

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

	for n in range(1,400):
		players = [] 
		for i in range(0,n):
			c = random.choice([BotRandom])
			players.append(c("P{}".format(i)))

		l = League(players)
		l.makeTables(0)

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
		players.append(ExShortSighted("X{}".format(i)))
		players.append(BotHonest("H{}".format(i)))
		players.append(BotUrchin("U{}".format(i)))
		players.append(BotUrchin("U{}".format(i)))

	l = League(players)


	for phaseIndex in range(0, Const.PHASES_PER_GAME):
		print ("\n\n\n--PHASE {}".format(phaseIndex))
		l.makeTables(phaseIndex)

		for roundIndex in range(0, Const.ROUNDS_PER_PHASE):
			print ("\n     ROUND {}.{}".format(phaseIndex, roundIndex))
			l.playRound(roundIndex)

def instantiateGame():

	a = Arena()
	a.runArena()

def gameStability(nbRuns):

	finalResults = []
	aiScores = {}
	for ai in Arena.availablePlayers:
		aiScores[ai] = []

	timeStart = datetime.datetime.now()

	for gameIndex in range (0, nbRuns):
		currentResult = ""
		a = Arena()
		a.runArena()


		ais = {}
		for p in a.league.humans:
			name = type(p).__name__
			if (name in  ais):
				if (p.wealth > ais[name].wealth):
					ais[name] = p
			else:
				ais[name] = p

		sorted(ais, key=lambda key:ais[key].wealth)
		index = 1
		for k,v in ais.items():
#			currentResult += "\n{:3} - {:6.2f}   {}".format(index, v.wealth, v.name)
			aiScores[type(v)].append(index)
			index += 1

		finalResults.append(currentResult)


	print ("")
	print ("Run for {}x{} rounds, {} INSTANCES_PER_PLAYER".format(Const.PHASES_PER_GAME, Const.ROUNDS_PER_PHASE, Const.INSTANCES_PER_PLAYER))
	print ("TIME {} to {}".format(timeStart, datetime.datetime.now()))



	sorted(aiScores, key=lambda k:sum(aiScores[k]))


	for k,v in aiScores.items():

		avg = sum(v)/len(v)
		var = sum((v[i]-avg)**2  for i in range(0, len(v))) / len(v)

		print ("{:30} : AVG = {:.3}  - StdDev = {:.3} \t- {}".format(
			k.__name__, 
			avg,
			var**0.5,
			v))


def gameStabilityCompared():

	for rnds in [2, 3]:
		for phases in [2, 3]:
			for insts in [5, 8]:
				Const.ROUNDS_PER_PHASE = rnds
				Const.PHASES_PER_GAME = phases
				Const.INSTANCES_PER_PLAYER = insts
				gameStability(20)




# Run tests

#smokeTest()
#populateTable()
#tablesDispatch()
#fullGame()
#instantiateGame()
#gameStability(60)

gameStabilityCompared()