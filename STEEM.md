## Coding contest: public goods problem

Submit your code, 90% payout split among winners (50/20/10/10)

Blockchain and crypto currencies have a lot to do with [Game Theory](https://en.wikipedia.org/wiki/Game_theory). For this very first coding contest on Steem, I invite you to submit your code for a bot that will play repeatedly a very simple game: the [*Public Goods Problem*](https://en.wikipedia.org/wiki/Public_goods_game). 

*(read the [french translation](./STEEM-fr.md))*

### Why A contest ?

The Steem network needs coders, professional and hobbyists alike. We need to develop bots, understand the blockchain, learn to program. And of course we need to have some fun. That's why I start this contest, time will tell if the idea takes off and if more contests will follow.

Also, we may be doing our little share in advancing the fields of games theory and experimental economy, which are so dear to us steemians.

Everybody is welcome to submit code. The more, the merrier.


### The Game

Very simple game indeed, and easy to play, even for AIs, and psychologically intense. Write a clever AI to play for you!

Each AI will be instantiated XXX times, each one will enter the game with *100 tokens* (completely virtual tokens, this is in no way real money)
Instances (players) will join tables of ten, then every AI on a table is asked to bet either *10 tokens*, *nothing*, or go *all in*. Then the bank will double the amount received and redistribute the total evenly among players, including those who gave nothing. 
Each table will play XXX rounds with the same players, where players know the history (but not the name) of their opponents, and can take decisions accordingly 
Players will be shuffled again to make new tables, and play a new XXX-round phase, a total of XXX times; playing a total of XXX (XXXxXXX) rounds. You'll have no information on what your opponents did on previous tables (just their current wealth)

At the end, the players will be ranked on the total wealth of their best instance.

And if you want to read more:
* [Wikipedia on the *Public Goods* game](https://en.wikipedia.org/wiki/Public_goods_game)
* [Wikipedia on game theory](https://en.wikipedia.org/wiki/Game_theory)
* [A very scientific article on nature.com](https://www.nature.com/articles/srep26889)

### Strategies

The payoff is maximum when all players on a table go all in, but this is a very risky move, and the richer players on the table won't like it altogether. Betting nothing may be a good decision in real life, but remember that the Arena only rewards the top 4 AIs. Build your own strategy, and be clever!


### The Rules

*(see a more detailed article on [the rules](./TEASER.md))*

Write a python class that inherits the `Player` class and submit it as a comment to this post. You can submit your code either directly in the comment text or as a link to a publicly accessible git repository ([Gist](gist.github.com) is a perfectly valid choice)

```
class Player:
    
    def __init__(self, name):
        self.id = ...                   # a random string
        self.wealth = Const.STARTING_WEALTH
        self.action = Bet.UNDECIDED
        self.decision = Bet.UNDECIDED


    def think(self, context):           # override this
        pass

```

Here's a very simple example. Meet your first opponent:

```
from Game.Player import Player
from Game.Context import Context
from Game.Bet import Bet

class ExamplePlayer(Player):

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


Each players will be instantiated XXX times and randomly assigned to tables for every phase. Assignment to table is *not* based on performance from previous phases. Approximately 20% short-lived bots will be added to fill holes, as evenly as possible. Bots will give ten 80% of the time and be recreated anew for each phase.

At the end, players will be ranked on the performance of *their best single instance*

Any player that tries to abuse the system, or consumes too much resources will be disqualified. No internet access is allowed. Code should be readable and commented

A player that tries to bet 10 while they have not enough wealth to do so will instead go all in. A player that fails to decide will also default to all in

The arena code is publicly available on [github](https://github.com/steemian/publicGood). Any comment/issue/pull request is most welcome. Minor changes and bugfixes may be added before the arena run

### The rewards

The arena will be executed in eight days, and the results published shortly after. All rewards from upvotes to this post and to my comments will be split between the winners:

1st player: 50% of total rewards
2nd player: 20%
3rd and 4th players: 10% each
10% are kept for myself

Of course, nothing prevents you from submitting an AI without upvoting to increase the prize pool. This is also part of the experiment. But given you have nothing to loose, it would be a bad move, wouldn't it?





