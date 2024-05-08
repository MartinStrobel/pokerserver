import time

from random import shuffle
from random import randint
import datetime
import sys, os
import pypokerengine
from pypokerengine.api import game




# Disable
def block_print():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enable_print():
    sys.stdout = sys.__stdout__

setup_config = game.setup_config
start_poker = game.start_poker

""" =========== *Remember to import your agent!!! =========== """
from Group23Player import Group23Player
from Group20Player import Group20Player
# from smartwarrior import SmartWarrior
""" ========================================================= """

""" Example---To run testperf.py with random warrior AI against itself. 

$ python testperf.py -n1 "Random Warrior 1" -a1 RandomPlayer -n2 "Random Warrior 2" -a2 RandomPlayer
"""


def two_player_game(agent_name1, agent1, agent_name2, agent2):
    # Init to play 500 games of 1000 rounds
    num_game = 1
    max_round = 1
    initial_stack = 10000
    smallblind_amount = 20

    # Init pot of players
    agent1_pot = 0
    agent2_pot = 0

    # Setting configuration
    config = setup_config(max_round=max_round, initial_stack=initial_stack, small_blind_amount=smallblind_amount)

    # Register players
    config.register_player(name=agent_name1, algorithm=agent1)
    config.register_player(name=agent_name2, algorithm=agent2)

    # Start playing num_game games
    block_print()
    for _ in range(1, num_game+1):
        game_result = start_poker(config, verbose=0)
        agent1_pot = agent1_pot + game_result['players'][0]['stack']
        agent2_pot = agent2_pot + game_result['players'][1]['stack']
    enable_print()

    if agent1_pot < agent2_pot:
        return agent_name2, agent_name1, agent2_pot - agent1_pot, agent1_pot, agent2_pot
    elif agent1_pot > agent2_pot:
        return agent_name1, agent_name2, agent1_pot - agent2_pot, agent1_pot, agent2_pot
    else:
        return agent_name1, agent_name2, agent1_pot - agent2_pot, agent1_pot, agent2_pot


def run_tournament():
    player_dict = players.make_player_dict()
    tournament = Tournament()
    tournament.startTime = datetime.datetime.now()
    tournament.save()
    keys = player_dict.keys()
    shuffle(keys)
    for _ in range(64 - len(keys)):
        keys.append(keys[randint(0, len(keys)-1)])
    print(len(keys))
    run_sub_tournament_level(player_dict, keys, 1, tournament)
    tournament.endTime = datetime.datetime.now()
    tournament.save()


def run_test_tournament(username):
    test_agent = players.get_player(username)
    random_agent = Group23Player()
    print("Testing {} player".format(username))
    print(two_player_game("Test",test_agent,"Random",random_agent))


def run_sub_tournament_level(player_dict, keys, level, tournament):
    print("##################{}###############".format(len(keys)))
    if len(keys) == 1:
        return player_dict[keys[0]]
    next_level = []
    fights = []
    for i in range(0, len(keys)-1, 2):
        tournament_fight = TournamentFight()
        tournament_fight.tournament_id = tournament
        tournament_fight.player1 = keys[i]
        tournament_fight.player2 = keys[i+1]
        tournament_fight.level = level
        tournament_fight.save()
        fights.append(tournament_fight)
    for fight in fights:
        winner, loser, margin, player1_pot, player2_pot = two_player_game(fight.player1, player_dict[fight.player1],
                                                                    fight.player2, player_dict[fight.player2])
        print(winner, loser, margin)
        fight.winner = winner
        fight.margin = margin
        fight.player1_pot = player1_pot
        fight.player2_pot = player2_pot
        fight.save()
        next_level.append(winner)
    return run_sub_tournament_level(player_dict, next_level, level+1, tournament)

print(two_player_game("23",Group23Player(),"23",Group23Player()))
