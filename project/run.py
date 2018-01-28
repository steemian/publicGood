from __future__ import print_function

import random
import datetime

from Game import *
from Contrib import *

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def runGame():

    a = Arena()
    a.runArena()


runGame()