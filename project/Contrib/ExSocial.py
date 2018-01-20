from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet
from Game.Const import Const

class ExSocial(Player):


	signature = [	
			Bet.NOTHING,
			Bet.TEN,
			Bet.TEN,
			Bet.NOTHING,
		]



	def friendlyMove(self, context, friends, roundIndex):
		if (len(friends) > 4):	# Nearly impossible, but worth trying
			print ("Social {} found optimal !!!".format(self.id))
			return Bet.ALLIN

		if (len(friends) > 2):
			if (self.id == self.bestInLine(friends)):
				print ("Social {} feels best in line of {}".format(self.id, len(friends)))
				return Bet.NOTHING
			else: 
				#print ("Social {} wants to help".format(self.id))
				return Bet.ALLIN

		# if not enough friends found, play it safe
		return Bet.TEN



	def isFriend(self, playerContext, roundIndex):

#		print (playerContext)
#		print (roundIndex)
#		print ("")

		if (playerContext.previousMoves[0:len(self.signature)] != self.signature):
			#print ("FRIEND TEST fail {}".format(playerContext.previousMoves))
			return False

		# TODO: could also check for later moves
		#print ("FRIEND TEST !!succeed!! for {} {}".format(playerContext.id, playerContext.previousMoves))
		return True




	def bestInLine(self, players):

		best = players[0]

		for p in players:
			if (p.wealth > best.wealth):
				best = p
			if (p.wealth == best.wealth and p.id < best.id):
				best = p

		return best.id



	def think(self, context):

		# First few rounds: play signature so that friends will idenify me
		if (context.roundIndex < len(self.signature)):
			return self.signature[context.roundIndex]

		# then count friends and coordinate if it's worth it
		friends = list(filter(lambda p:self.isFriend(p, context.roundIndex), context.playerContexts.values()))

#		if (len(friends) > 0):
#			print (context.describe())

		move = self.friendlyMove(context, friends, context.roundIndex)
		print ("SOCIAL move {} {}".format(self.id, move.name))

		return move

