import time
#import players
from random import shuffle
from random import randint
import datetime
import sys, os, json
import pypokerengine
from pypokerengine.api import game
from randomplayer import RandomPlayer





# Disable
def block_print():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enable_print():
    sys.stdout = sys.__stdout__

setup_config = game.setup_config
start_poker = game.start_poker


def get_player(name):
    if name=="1":
        from StudentAgentFinalUploads.Poker01.Group01Player import Group01Player
        return Group01Player()
    if name=="2":
        from StudentAgentFinalUploads.Poker02.Group02Player import Group02Player
        return Group02Player()
    if name=="3":
        from StudentAgentFinalUploads.Poker03.Group03Player import Group03Player
        return Group03Player()
    if name=="4":
        from StudentAgentFinalUploads.Poker04.Group04Player import Group04Player
        return Group04Player()
    if name=="5":
        from StudentAgentFinalUploads.Poker05.Group05Player import Group05Player
        return Group05Player()
    if name=="6":
        from StudentAgentFinalUploads.Poker06.Group06Player import Group06Player
        return Group06Player()
    if name=="7":
        from StudentAgentFinalUploads.Poker07.Group07Player import Group07Player
        return Group07Player()
    if name=="8":
        from StudentAgentFinalUploads.Poker08.Group08Player import Group08Player
        return Group08Player()
    if name=="9":
        from StudentAgentFinalUploads.Poker09.Group09Player import Group09Player
        return Group09Player()
    if name=="10":
        from StudentAgentFinalUploads.Poker10.Group10Player import Group10Player
        return Group10Player()
    if name=="11":
        from StudentAgentFinalUploads.Poker11.Group11Player import Group11Player
        return Group11Player()
    if name=="12":
        from StudentAgentFinalUploads.Poker12.Group12Player import Group12Player
        return Group12Player()
    if name=="13":
        from StudentAgentFinalUploads.Poker13.Group13Player import Group13Player
        return Group13Player()
    if name=="14":
        from StudentAgentFinalUploads.Poker14.Group14Player import Group14Player
        return Group14Player()
    if name=="15":
        from StudentAgentFinalUploads.Poker15.Group15Player import Group15Player
        return Group15Player()
    if name=="16":
        from StudentAgentFinalUploads.Poker16.Group16Player import Group16Player
        return Group16Player()
    if name=="17":
        from StudentAgentFinalUploads.Poker17.Group17Player import Group17Player
        return Group17Player()
    if name=="18":
        from StudentAgentFinalUploads.Poker18.Group18Player import Group18Player
        return Group18Player()
    if name=="19":
        from StudentAgentFinalUploads.Poker19.Group19Player import Group19Player
        return Group19Player()
    if name=="20":
        from StudentAgentFinalUploads.Poker20.Group20Player import Group20Player
        return Group20Player()
    if name=="21":
        from StudentAgentFinalUploads.Poker21.Group21Player import Group21Player
        return Group21Player()
    if name=="22":
        from StudentAgentFinalUploads.Poker22.Group22Player import Group22Player
        return Group22Player()
    if name=="23":
        from StudentAgentFinalUploads.Poker23.Group23Player import Group23Player
        return Group23Player()
    if name=="24":
        from StudentAgentFinalUploads.Poker24.Group24Player import Group24Player
        return Group24Player()
    if name=="25":
        from StudentAgentFinalUploads.Poker25.Group25Player import Group25Player
        return Group25Player()
    if name=="26":
        from StudentAgentFinalUploads.Poker26.Group26Player import Group26Player
        return Group26Player()
    if name=="27":
        from StudentAgentFinalUploads.Poker27.Group27Player import Group27Player
        return Group27Player()
    if name=="28":
        from StudentAgentFinalUploads.Poker28.Group28Player import Group28Player
        return Group28Player()
    if name=="30":
        from StudentAgentFinalUploads.Poker30.Group30Player import Group30Player
        return Group30Player()
    if name=="31":
        from StudentAgentFinalUploads.Poker31.Group31Player import Group31Player
        return Group31Player()
    if name=="32":
        from StudentAgentFinalUploads.Poker32.Group32Player import Group32Player
        return Group32Player()
    if name=="33":
        from StudentAgentFinalUploads.Poker33.Group33Player import Group33Player
        return Group33Player()
    if name=="35":
        from StudentAgentFinalUploads.Poker35.Group35Player import Group35Player
        return Group35Player()
    if name=="36":
        from StudentAgentFinalUploads.Poker36.Group36Player import Group36Player
        return Group36Player()
    if name=="40":
        from StudentAgentFinalUploads.Poker40.Group40Player import Group40Player
        return Group40Player()
    if name=="42":
        from StudentAgentFinalUploads.Poker42.Group42Player import Group42Player
        return Group42Player()
    if name=="44":
        from StudentAgentFinalUploads.Poker44.Group44Player import Group44Player
        return Group44Player()
    if name=="45":
        from StudentAgentFinalUploads.Poker45.Group45Player import Group45Player
        return Group45Player()
    if name=="46":
        from StudentAgentFinalUploads.Poker46.Group46Player import Group46Player
        return Group46Player()
    if name=="47":
        from StudentAgentFinalUploads.Poker47.Group47Player import Group47Player
        return Group47Player()
    if name=="48":
        from StudentAgentFinalUploads.Poker48.Group48Player import Group48Player
        return Group48Player()
    if name=="49":
        from StudentAgentFinalUploads.Poker49.Group49Player import Group49Player
        return Group49Player()
    if name=="50":
        from StudentAgentFinalUploads.Poker50.Group50Player import Group50Player
        return Group50Player()


def get_settings(setting):
    return json.loads(setting)




def two_player_game(agent_name1, agent1, agent_name2, agent2):
    num_game = settings["num_game"]
    max_round = settings['max_round']
    initial_stack = settings['initial_stack']
    smallblind_amount = settings['smallblind_amount']

    


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
        return "###123###{}###123###{}###123###{}###123###".format(agent_name2, agent_name1, agent2_pot - agent1_pot)
    elif agent1_pot > agent2_pot:
        return "###123###{}###123###{}###123###{}###123###".format(agent_name1, agent_name2, agent1_pot - agent2_pot)
    else:
        return "###123###{}###123###{}###123###{}###123###".format(agent_name1, agent_name2, agent1_pot - agent2_pot)




args = sys.argv
if len(sys.argv) < 4:
    print("Not enough arguments")
player1 = get_player(args[1])
player2 = get_player(args[2])
settings = get_settings(args[3])
print(two_player_game(args[1],player1,args[2],player2))
