import time
import players
from random import shuffle
from random import randint
import subprocess
import datetime
import sys, os, inspect
import pypokerengine
import json
from pypokerengine.api import game
from django.utils.module_loading import import_module
from django.contrib.auth.models import User
from ..models import Tournament, TournamentFight, Setting, FinalTournamentResult, Final2TournamentResult


# Disable
def block_print():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enable_print():
    sys.stdout = sys.__stdout__

setup_config = game.setup_config
start_poker = game.start_poker

""" =========== *Remember to import your agent!!! =========== """
from randomplayer import RandomPlayer
# from smartwarrior import SmartWarrior
""" ========================================================= """

""" Example---To run testperf.py with random warrior AI against itself. 

$ python testperf.py -n1 "Random Warrior 1" -a1 RandomPlayer -n2 "Random Warrior 2" -a2 RandomPlayer
"""


def final_two_player_game(player1, player2,startPlayer):
    filepath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/"
    setting = Setting.objects.latest('endTime')
    settings = {'num_game': setting.num_game, 'max_round': setting.max_round, 'initial_stack': setting.initial_stack , 'smallblind_amount': setting.smallblind_amount}
    outfile = open(filepath+"finalSubprocessOutput{}.txt".format(startPlayer),"w")
    errorfile = open(filepath+"finalSubprocessErrorOutput{}.txt".format(startPlayer),"w")
    timeout = 1200
    returncode = subprocess.call([filepath+"finalTournamentScript.sh",
    str(player1),str(player2),json.dumps(settings).replace(" ", ""),str(timeout)],
        stdout=outfile,stderr=errorfile)
    outfile.close()
    errorfile.close()
    print(returncode)
    if returncode:
        print("Error")
        outfile = open(filepath+"finalSubprocessErrorOutput{}.txt".format(startPlayer),"r")
        result = outfile.read()
        return {"outcome":"Error","message":result}
    else:
        print("Success")
        outfile = open(filepath+"finalSubprocessOutput{}.txt".format(startPlayer),"r")
        result = outfile.read()
        if "Timeout" in result:
            return {"outcome":"Timeout"}
        else:
            winner = result.split("###123###")[1]
            loser  =  result.split("###123###")[2]
            gap  =  int(result.split("###123###")[3])
            return {"outcome":"Win","winner":winner,"loser":loser,"profit":gap/2}

def two_player_game(agent_name1, agent1, agent_name2, agent2):
    # Init to play 500 games of 1000 rounds
    setting = Setting.objects.latest('endTime')
    num_game = setting.num_game
    max_round = setting.max_round
    initial_stack = setting.initial_stack
    smallblind_amount = setting.smallblind_amount

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

def alreadyFought(user1,user2):
    wins = user1.wins2.all()
    for win in wins:
        if win.loser_id == user2:
            return True
    losses = user1.losses2.all()
    for los in losses:
        if los.winner_id == user2:
            return True
    return False

def run_final_tournament(startPlayer):
    #FinalTournamentResult.objects.all().delete()
    final_tournament_errors = open(str(startPlayer)+"finalTournamentErrors.txt","w")
    users = User.objects.filter(username__contains="Group").order_by('username')
    for i,user1 in enumerate(users[startPlayer:startPlayer+5]):
        for user2 in users[i+startPlayer+1:]:
            user1_number = int(user1.username[5:7])
            user2_number = int(user2.username[5:7])
            print("{} vs {}".format(user1.username,user2.username))
            if alreadyFought(user1,user2):
                print("Already fought")
                continue
            result = final_two_player_game(user1_number,user2_number,str(startPlayer))
            final_tournament_result = Final2TournamentResult()
            if result['outcome'] =="Win":
                final_tournament_result.outcome = "Win"
                if int(result['winner']) == int(user1_number):
                    final_tournament_result.winner_id  = user1
                    final_tournament_result.loser_id   = user2
                elif int(result['winner']) == int(user2_number): 
                    final_tournament_result.winner_id  = user2
                    final_tournament_result.loser_id   = user1
                else:
                    final_tournament_result.outcome = "Error"
                final_tournament_result.profit  = result['profit']
                final_tournament_result.save()
            elif result['outcome'] =="Timeout":
                final_tournament_result.outcome = "Timeout"
                final_tournament_result.save()
            else:
                final_tournament_result.outcome = "Error"
                final_tournament_result.save()
                final_tournament_errors.write("########################\n")
                final_tournament_errors.write("########################\n")
                final_tournament_errors.write("##### {} ######### {}  ####\n".format(i,j))
                final_tournament_errors.write("########################\n")
                final_tournament_errors.write("########################\n")
                final_tournament_errors.write(result)
    final_tournament_errors.close()

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
    random_agent = RandomPlayer()
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

