from enum import Enum

class Bet(Enum):
    UNDECIDED = 0
    TEN = 1                 # TODO: use a constant
    NOTHING = 3
    ALLIN = 4


    def asChar(self):
        if (self == Bet.NOTHING):
            return "0"
        if (self == Bet.TEN):
            return "1"
        if (self == Bet.ALLIN):
            return "A"
        if (self == None):
            return "."
        if (self == UNDECIDED):
            return "?"

