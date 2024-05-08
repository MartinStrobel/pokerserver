#!/bin/bash
source cs3243projectenv/bin/activate
if timeout $4 python kingOfTheHill/mypoker/final_two_player_game.py $1 $2 $3 ; then
	echo "Success"
else
	echo "Timeout"	
fi