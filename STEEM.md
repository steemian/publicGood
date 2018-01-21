## The AI Contest #1: public goods problem

Submit your code, 90% payout split among winners (50/20/10/10)
<center>
![AiContest](https://s19.postimg.org/c40evtcxf/code_Blur.png)
</center>

![French](https://s9.postimg.org/3mpd3j2sf/flag-fr-qc_14x21.png) *(read the [french translation](./STEEM-fr.md))*

Blockchain and crypto currencies have a lot to do with [Game Theory](https://en.wikipedia.org/wiki/Game_theory). For this very first coding contest on Steem, I invite you to submit your code for a bot that will play repeatedly a very simple game: the [*Public Goods Problem*](https://en.wikipedia.org/wiki/Public_goods_game). 


### Why A contest ?

*(read more on [AI Contest introductory post](./TEASER.md))*


The Steem network needs coders, professional and hobbyists alike. We need to develop bots, understand the blockchain, learn to program. And of course we need to have some fun. That's why I start this contest, others will follow every week.

Also, we may be doing our little share in advancing the fields of games theory and experimental economy, which are so dear to us steemians.

Everybody is welcome to submit code. The more, the merrier. Non-programmers are welcome too (see below)


### The Game

Very simple game indeed, and easy to play, even for AIs, and psychologically intense. Will you cooperate or live on the land? Write a clever AI to play for you!

<center>
![Public goods](https://s19.postimg.org/jvlq7uj8j/public-goods-smaller.png)
</center>

Each turn, contribute to a common fund (by giving away tokens), or not. The bank then doubles the total fund and redistributes evenly among all participants. Maybe it rings a bell for you steemians?

Richest AI (token-wise) when the game ends wins

And if you want to read more:
* [Wikipedia on the *Public Goods* game](https://en.wikipedia.org/wiki/Public_goods_game)
* [Wikipedia on game theory](https://en.wikipedia.org/wiki/Game_theory)
* [A very scientific article on nature.com](https://www.nature.com/articles/srep26889)

### The Arena (where your AIs will compete)

Write a python class that inherits `Player` (see below) and submit it as a comment to this post. If you don't know Python, or if you can't write programs at all you can still participate, just read on. You can submit your code either directly in the comment text or as a link to a publicly accessible git repository ([Gist](gist.github.com) is a great choice)

In a week, I will run the arena code (you can have a look [here](https://github.com/steemian/publicGood) although it may change before the Arena run), publish the leaderboard and split the rewards

### What if I'm not a programmer

Post your solution anyway! There are lots of programmers around (including myself) who will gladly translate your idea. Be careful to be very precise in your description though: programmers like it clear

Alternatively, this is a great time to start learning. Ask around or [look for a Python quick tutorial](https://www.google.fr/search?q=python+quick+tutorial)

<center>
![Let's get coding](https://s19.postimg.org/tswr14oc3/code-400.jpg)
</center>

### Let's get coding

Each AI will be instantiated `INSTANCES_PER_PLAYER` times, and you will be rated by the performance of *your single best performing instance*. Each one will enter the game with *`STARTING_WEALTH` money tokens*. Instances (players) will join tables of `PLAYERS_PER_TABLE`, with about 20% short lived bots to fill tables. Bots are destroyed after each phase and contribute 80% of the time

Assignment to table is random and *not* based on performance from previous phases

Once players sit on the table, everyone is asked to bet either *10 tokens*, *nothing*, or go *all in*. Then the bank will double the amount received and redistribute the total evenly among players, including those who gave nothing 

Each table will play `ROUNDS_PER_PHASE` rounds with the same players (learn to know each other), where players know the history (but not the name) of their opponents, and can take decisions accordingly. Players will be shuffled again to make new tables (with new bots), and play a new `ROUNDS_PER_PHASE`-round phase, a total of `PHASES_PER_GAME` times; playing a total of (`PHASES_PER_GAME` x `ROUNDS_PER_PHASE`) rounds. You'll have no information on what your opponents did on previous tables (only their current wealth)

At the end, players will be ranked on the performance of *their best single instance*


```
    PLAYERS_PER_TABLE = 10
    INSTANCES_PER_PLAYER = 12
    ROUNDS_PER_PHASE = 15
    PHASES_PER_GAME = 10
    STARTING_WEALTH = 100
```


### Override this

```
class Player:
    
    def __init__(self, name):
        self.id = ...                   # a random string
        self.wealth = Const.STARTING_WEALTH
        self.action = Bet.UNDECIDED
        self.decision = Bet.UNDECIDED

    def getSteemUser(self):             # override this to return your steem name
        pass                            

    def think(self, context):           # override this
        pass
```

Your decision should return

```
class Bet(Enum):
    TEN = 1
    NOTHING = 3
    ALLIN = 4
```

Here's a very simple example. Meet your first opponent:

```
from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ExamplePlayer(Player):

    def getSteemUser(self):
        return "@gbd"

    def think(self, context):
        # First round: bet a regular ten
        if (context.roundIndex == 0):
            return Bet.TEN

        # Subsequent rounds: bet ten unless your opponents are rats
        nbUrchins = sum(c.previousMoves[context.roundIndex-1] == Bet.NOTHING 
                        for c in context.playerContexts.values())
        nbPlayers = len(context.playerContexts.values())
        if (nbUrchins > 2):
            return Bet.NOTHING
        else:
            return Bet.TEN
```

A fresh copy of the context object will be provided with all informations you need (updated every round):

``` 
class PlayerContext:
#   wealth = 0;             # this player current wealth, as a float
#   previousMoves = []      # a list of the moves this player made during previous rounds
#   id = ""                 # a random string. Yours is Player.id

class Context:
#   playerContexts = {} # a dictionary of (Player.id : playerContext). Some are bots
#   payouts = []        # a list of the payouts for every past round of this phase
#   roundIndex = 0      # out of Const.ROUNDS_PER_PHASE
#   phaseIndex = 0      # out of PHASES_PER_GAME
#   totalHumans = 0     # total number of AI (non-filler-bots) in the whole Arena
#   totalBots = 0       # total number of filler bots. Those are recreated every phase
#   tableIndex = 0      # identify the table you're in
```


Any player that trying to abuse the system, or consumes too much resources will be disqualified. No internet access is allowed. Code should be readable and commented

A player that tries to bet 10 while they have not enough wealth to do so will instead go all in. A player that fails to decide will also default to all in

The arena code is publicly available on [github](https://github.com/steemian/publicGood). Any comment/issue/pull request is most welcome. Minor changes and bugfixes may be added before the arena run

### The Strategy

<center>
![Strategy](https://s19.postimg.org/7tqcdqzqb/rubik-500.jpg)
</center>

The payoff is maximum when all players on a table go all in, but, well, do you really expect your opponents o be that generous? Betting nothing may be a good decision in real life, but remember that the Arena only rewards the top 4. Betting ten is a shy and safe move, but won't make a fortune either. And even if you want to help others (strange idea) by going all in, you'd better choose well the time for that.

Build your own strategy, and be clever!


### The rewards

The arena will be executed in eight days, and the results published manually shortly after. All rewards from upvotes to this post, its translations, the [introductory post](./TEASER.md) and to my comments will be split between the winners:

* 1st player: 50% of total rewards
* 2nd player: 20%
* 3rd and 4th players: 10% each
* 10% are kept for myself

Of course, nothing prevents you from submitting an AI without upvoting to increase the prize pool. This is also part of the experiment. But given you have nothing to loose, it would be a bad move, wouldn't it?

*Do you think this contest is useful for the community? Tell me your opinion!*

*(many thanks to the authors I link to, including anonymous Wikipedians)*

### Read my previous posts

* *[the AI Contest Introduction post](./TEASER.md))* (or [in French](./TEASER-fr.md) ![French](https://s9.postimg.org/3mpd3j2sf/flag-fr-qc_14x21.png))
