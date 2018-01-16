## Coding contest: public goods problem

Submit your code, 90% payout split among winners (50/20/10/10)

Blockchain and crypto currencies have a lot to do with [Game Theory](https://en.wikipedia.org/wiki/Game_theory). For this very first coding contest on Steem, I invite you to submit your code for a bot that will play repeatedly a very simple game, which is a good illustration on Game Theory: the [*Public Goods Problem*](https://en.wikipedia.org/wiki/Public_goods_game). 

### Why A contest ?

The Steem network needs coders, professional and hobbyists alike. We need to develop bots, understand the blockchain, learn to program. And of course we need to have some fun. That's why I start this contest, time will tell if the idea takes off and if more contests will follow.

Also, we may be doing our little share in advancing the fields of games theory and experimental economy, which are so dear to us steemians.

Everybody is welcome to submit code. The more, the merrier.


### The Game

Very simple game indeed, and easy to play, even for bots. 

Each player will enter the game with *100 tokens* (completely virtual tokens, this is in no way real money)
Players will join tables of ten, then every player on a table is asked to bet either *10 tokens*, *nothing*, or go *all in*. Then the bank will double the amount received and redistribute the total evenly among players, including those who bet nothing. 
Each table will play twelve rounds with the same players, where players know the history (but not the name) of their opponents, and can take decisions accordingly. 
Players will be shuffled again to make new tables, and play a new 12-round phase, a total of five times; playing a total of 60 (5x12) rounds.

At the end, the players will be ranked on the total wealth of their best instance (see below).


### Strategies

The payoff is maximum when all players on a table go all in, but this is a very risky move, and the richer players on the table won't like it altogether. Betting nothing may be a good decision in real life, but remember that the game only rewards the top 4 players. Build your own strategy!


### The Contest

Write a python class that inherits the `Player` class and submit it as a comment to this post. You can submit your code either directly in the comment text or as a link to a publicly accessible git repository ([Gist](gist.github.com) is a perfectly valid choice)

Each players will be instantiated 3 times and randomly assigned to tables for every phase. Assignment to table is *not* based on performance from previous phases. Players will be ranked on the performance of *their best single instance*.

Any player that tries to abuse the system, or consumes too much resources will be disqualified.

A player that tries to bet 10 while they have not enough wealth to do so will instead go all in

### The rewards

The arena will be executed in eight days, and the results published shortly after. All rewards from upvotes to this post and to my comments will be split between the winners:

1st player: 50% of total rewards
2nd player: 20%
3rd and 4th players: 10% each
10% are kept for myself

Of course, nothing prevents you from submitting a bot without upvoting to increase the prize pool. This is also part of the experiment. But given you have nothing to loose, it would be a bad move, wouldn't it?





