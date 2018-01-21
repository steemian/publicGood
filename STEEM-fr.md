## The AI Contest #1: Le dilemme des biens communs

Postez votre AI, 90% des récompenses partagées entre les gagnants

<center>
![AiContest](https://s19.postimg.org/c40evtcxf/code_Blur.png)
</center>

![English](https://s19.postimg.org/ezi3gi6c3/UK-_US_flag-21.png) *([Article en anglais](./STEEM.md))*

Les cryptomonnaies sont une application de la [théorie des jeux](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_jeux). Etudions ensemble pour mieux comprendre Steem et les steemiens

POur ce premier concours, je vous invite à décrire une intelligence artificielle qui joue à un jeu très simple, application basique de la théorie des jeux: le [Dilemme des Biens Communs](https://fr.wikipedia.org/wiki/Trag%C3%A9die_des_biens_communs)


### Un concours ?

*(plus d'infos sur [mon introduction à The AI Contest](./TEASER-fr.md))*

STEEM a besoin de programmeurs, professionnels comme amateurs. Il y a toujours besoin de développer ou d'améliorer un bot, comprendre un peu mieux la blockchain ou simplement apprendre à programmer. CQFD

Et au passage, si ce concours peut aider à mieux comprendre la théorie des jeux, la psychologie des humains, l'économie en général ou juste la blockchain, c'est toujours ça de gagné pour l'humanité et pour STEEM.

Toute contribution est la bienvenue, même les programmeurs débutants, même les non-programmeurs (voir plus bas)


### Le Jeu

C'est un jeu très basique, une simple illustration de la théorie. Facile à jouer pour une intelligence artificielle, et néanmoins intense psychologiquement. Allez-vous coopérer pour le bien commun, ou rester oisif et profiter du travail des autres? 

<center>
![Public goods](https://s19.postimg.org/jvlq7uj8j/public-goods-smaller.png)
</center>

Chaque tour, chaque joueur peut contribuer au bien commun en donnant des jetons virtuels, ou non. La banque double ensuite le total et redistribue à tous les joueurs, y compris ceux qui n'ont rien donné. Un peu comme dans l'économie réelle, et beaucoup comme sur STEEM.

L'AI la plus riche (en jetons) à la fin du jeu remporte les gains

Pour aller plus loin:
* [Wikipedia, la *Tragédie des biens communs*](https://fr.wikipedia.org/wiki/Trag%C3%A9die_des_biens_communs)
* [Wikipedia, les *Jeux à somme nulle*](https://fr.wikipedia.org/wiki/Jeu_%C3%A0_somme_nulle)
* [Pour les acharnés et anglophones, un article de *nature*](https://www.nature.com/articles/srep26889)

### L'Arène des AIs

Pour participer, écrivez une classe Python qui hérite de `Player` (voir plus bas) et postez-la comme commentaire. Si vous ne savez pas programmer en Python (ou pas du tout) vous pouvez participer quand même, continuez à lire. Votre commentaire peut contenir du code, un lien [Gist](gist.github.com) ou git, ou une description textuelle de votre AI.

Dans une semaine, j'exécuterai le [code de l'Arène](https://github.com/steemian/publicGood), je publierai les vainqueurs et je redistribuerai les récompenses

### Pour ceux qui ne parlent pas Python couramment

Postez votre solution en bon français. Il y a beaucoup de programmeurs qui se feront un plaisir de vous aider (moi le premier). Soyez précis dans votre description, les programmeurs sont parfois obtus!

Ou bien [apprenez à programmer](https://www.google.fr/search?q=python+quick+tutorial). C'est le moment!

<center>
![Let's get coding](https://s19.postimg.org/tswr14oc3/code-400.jpg)
</center>

### Au boulot !

Chaque AI sera instanciée `INSTANCES_PER_PLAYER` fois, et votre score final sera celui de votre meilleure instance. Chaque instance entre dans l'arène avec *`STARTING_WEALTH` jetons*. Les instances (ou joueurs) seront réparties en tables de `PLAYERS_PER_TABLE`, avec environ 20% de bots pour combler les trous. Les bots sont détruits à la fin de chaque phase et contribuent 80% du temps.

La répartition des tables est aléatoire, et *ne dépend pas des scores*

Une fois les joueurs installés, chacun contribue de *10 jetons*, de *rien du tout*, ou de *toute sa fortune*. La banque additionne le tout, *double le montant* et redistribue l'ensemble en parts égales à tous les joueurs, même ceux qui n'ont rien donné.

Chaque table joue `ROUNDS_PER_PHASE` rounds avec les mêmes joueurs (le temps d'apprendre à se connaître). L'historique de chaque joueurs *sur la table courante* est fourni par un objet `Context`. Les informations de leur table précédente ne sont pas disponibles. Une fois tous les rounds joués, les joueurs sont de nouveau répartis en tables (avec des nouveaux bots), un total de `PHASES_PER_GAME` fois. Chaque instance aura donc joué (`PHASES_PER_GAME` x `ROUNDS_PER_PHASE`) rounds en tout.

Après la dernière phase, les AIs seront classés selon les performances de leur meilleure instance

```
    PLAYERS_PER_TABLE = 10
    INSTANCES_PER_PLAYER = 12
    ROUNDS_PER_PHASE = 15
    PHASES_PER_GAME = 10
    STARTING_WEALTH = 100
```


### Override la classe Player

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

Votre décision (`think()`) doit retourner

```
class Bet(Enum):
    TEN = 1
    NOTHING = 3
    ALLIN = 4
```

Un exemple simple, qui sera votre premier adversaire:

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

Les informations disponibles sont fournies par:

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


Une AI qui tente d'abuser du système, de communiquer apr internet, ou qui consomme trop de ressources de calcul sera disqualifiedlifiée. Le code doit être lisible et compréhensible.

Un joueur qui tente de miser plus que ce qu'il a, ou qui ne fournit pas de décision claire *sera considéré comme mettant son tapis*

Le code est disponible sur [github](https://github.com/steemian/publicGood). Tout commentaire, bug report ou pull request est le bienvenu. Le code peut changer avant l'exécution de l'arène

### Stratégie

<center>
![Strategy](https://s19.postimg.org/7tqcdqzqb/rubik-500.jpg)
</center>

Le plus gros gain possible se passe quand tout le monde joue tapis, mais est-il raisonnable d'espérer ça de vos adversaires? Jouer l'avarice marche dans la vraie vie (helas), mais n'oubliez pas que la récompense est seulement pour les quatre premiers. Donner dix est une stratégie valide, mais ça ne construit pas la fortune. Et même si vous voulez tout donner pour aider les autres (vous pouvez), encore faut-il bien choisir le moment. Soyez malins!


### Système de récompenses

L'Arène sera exécutée dans huit jours, et les résultats publiés (manuellement). Toutes les récompenses des upvotes (sur ce post, ses traductions, le [post d'introduction](./TEASER-fr.md) et mes commentaires) seront répartis en:

* 1ere AI au classement: 50% du total
* 2e AI: 20%
* 3e et 4e: 10% chaque
* 10% pour moi

Bien sûr, personne ne vous oblige à voter si vous postez une AI. C'est en soi un cas intéressant de problème des biens communs. Mais vous n'avez pas grand chose à perdre...

*Vous pensez que ce concours est utile à la communauté? Donnez votre avis!*

*(remerciements à tous les auteurs que je cite ici, en particulier les wikipediens)*

### Mes posts précédents

* *[Introduction au AI Challenge](./TEASER-fr.md))* ([version anglaise](./TEASER.md) ![English](https://s19.postimg.org/ezi3gi6c3/UK-_US_flag-21.png) *([Article en anglais](./STEEM.md))*
)
