from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class OffendablePlayer(Player):
    """
    simple bot that "takes offense" if number of players that bet is
    less that number of players that don't * OFFENSIVENESS factor
    """

    OFFENSIVENESS = 3
    def getSteemUser(self):
        return "@scorpil"

    def think(self, context):
        moves = {
            Bet.TEN: 0,
            Bet.NOTHING: 0,
            Bet.ALLIN: 0,
        }
        for pl in context.playerContexts.values():
            if len(pl.previousMoves):
                bet = pl.previousMoves[-1]
                moves[bet] = moves.get(bet, 0) + 1

        pos_score = moves[Bet.TEN] + moves[Bet.ALLIN]
        neg_score = moves[Bet.NOTHING] * self.OFFENSIVENESS
        if pos_score >= neg_score:
            return Bet.TEN
        return Bet.NOTHING