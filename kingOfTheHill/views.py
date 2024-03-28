# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UploadFileForm, StartFinalTournamentForm
from .models import King, Profile, Tournament, TournamentFight, Setting, GroupUpload, Final2TournamentResult
import mypoker.tournaments
from background_task import background


import traceback
import datetime
import time
import random
import os
import sys
import numpy as np
from os.path import expanduser
home = expanduser("~")
from shutil import copyfile

# Create your views here.
currentKingPath = 'CurrentKing/currentKing.py'


def home_view(request):
    user = request.user
    if request.user.is_anonymous:
        return render(request, 'upload.html', {'haveMessage': False})
    now = datetime.datetime.today()
    last_submission = user.profile.last_submission
    if last_submission is None or (now.date() - last_submission).days > 0:
        user.profile.num_sub = 0

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            return handle_uploaded_file(request.FILES['file'], request)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form,
                                           'num_sub': user.profile.num_sub,
                                           'status' : user.profile.status,
                                           'last_sub': user.profile.last_submission,
                                           'haveMessage': False})


def user_view(request):
    if request.user.is_anonymous:
        return render(request, 'upload.html', {'haveMessage': False})
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user.html', {
        'form': form
    })


def ranking_view(request):
    if request.user.is_anonymous:
        return render(request, 'upload.html', {'haveMessage': False})
    user = request.user
    last_tournament = Tournament.objects.latest('startTime')
    setting = Setting.objects.latest('endTime')
    tournament_fights = last_tournament.fights.all().order_by('id')
    level_counter = 1
    levels = []
    current_level = []
    for fight in tournament_fights:
        if fight.level > level_counter:
            levels.append(current_level)
            current_level = []
            level_counter += 1
        fight.level = 2**(level_counter - 1)
        current_level.append(fight)
    levels.append(current_level)
    winner = fight.winner
    if request.method == 'POST':
        run_new_tournament()
        return redirect('ranking')
    martin = False
    if user.username == "martin" or user.username == "Yair" :
        martin = True
    return render(request, 'tournament.html', {'fights': levels, 'haveMessage': False,
                                               'tournament': last_tournament, 'winner': winner,
                                               'martin': martin, 'setting': setting})


def final_tournament_view(request):
    form = StartFinalTournamentForm()
    current_user = request.user
    setting = Setting.objects.latest('endTime')
    users = User.objects.filter(username__contains="Group").order_by('username')
    if request.method == 'POST':
        for start_player in [0,5,10,15,20,25,30,35,40]:
            run_final_tournament(start_player)
        return redirect('Final tournament')
    martin = False
    profits = []
    nums_opponents = []
    number = -1
    for counter,user in enumerate(users):
        number_opponents = 0
        if str(current_user) == str(user) :
            number = counter
        user.profit = 0
        user.opponents = {}
        for user2 in users:
            user.opponents[str(user2)] = "N.A."
        for win in user.wins.all():
            number_opponents = number_opponents + 1
            user.profit = user.profit + win.profit
            user.opponents[str(win.loser_id)] = win.profit
        for los in user.losses.all():
            number_opponents = number_opponents + 1
            user.profit = user.profit - los.profit
            user.opponents[str(los.winner_id)] = -los.profit
        opponents = []
        for user2 in users:
            opponents.append(user.opponents[str(user2)])
        user.opponents = opponents 
        if number_opponents > 0:
           profits.append(user.profit / number_opponents)
           nums_opponents.append(number_opponents)
        else :
           profits.append(0)
           nums_opponents.append(0)
    money_made = ""
    position = len(users) + 1 
    number_users = len(users)
    argsorted_position = np.asarray(profits).argsort()
    ranks = []
    for i,j in enumerate(argsorted_position):
        if j < 29-1 :
            modifier = 0
        elif j < 34-2:
            modifier = 1
        elif j < 37-3:
            modifier = 2
        elif j < 38 -4:
            modifier = 3
        elif j < 39 -5:
            modifier = 4
        elif j < 41 -6 :
            modifier = 5
        elif j < 43 -7 :
            modifier = 6
        else:
            modifier = 7

        rank = {"rank": 43-i, "group": "Group{:02d}".format(j+1+modifier), "profit":profits[j],
                "num_fights":nums_opponents[j]}
        ranks = [rank] + ranks
        if number != -1 and j== number:
            money_made = profits[number]
            position = i
    position = "{}/{}".format(number_users-position,number_users)
        
    current_best = "Group{:02d}".format(np.asarray(profits).argmax()+1)

    finalFights = Final2TournamentResult.objects.all() 
    results = np.zeros([50,50])
    numberOfGames = np.zeros([50,50])
    for fight in finalFights:
    	if(fight.outcome == "Win"):
    		winner_id = int(str(fight.winner_id)[5:]) - 1
    		loser_id = int(str(fight.loser_id)[5:]) -1
    		results[winner_id,loser_id] += fight.profit
    		results[loser_id,winner_id] -= fight.profit
    		numberOfGames[winner_id,loser_id] += 1
    		numberOfGames[loser_id,winner_id] += 1
    results = results/numberOfGames

    if current_user.username == "martin" or current_user.username == "Yair" :
        martin = True
    return render(request, 'finaltournament.html', {'user': current_user, 'current_best': current_best, 'money_made':money_made , 'position':position, 'groups': users, 'haveMessage': False,
                                               'martin': martin, 'setting': setting, 'ranks': ranks, 'form': form , 'finalFights': finalFights, 'results':results})


def additional_upload_view(request):
    user = request.user
    user_uploads = user.uploads.all().order_by('id')
    if request.user.is_anonymous:
        return render(request, 'upload.html', {'haveMessage': False})


    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            return handle_uploaded_additional_file(request.FILES['file'], request)
    else:
        form = UploadFileForm()
    return render(request, 'uploadAdditional.html', {'form': form,
                                           'status' : user.profile.status,
                                           'uploads': user_uploads,
                                           'haveMessage': False})


@background(schedule=5)
def run_new_tournament():
    mypoker.tournaments.run_tournament()

@background(schedule=5)
def run_final_tournament(start_player):
    mypoker.tournaments.run_final_tournament(start_player)


src = home+'/cs3243project/kingOfTheHill/mypoker/StudentAgentUploadsTemp/{}Player.{}'
dst = home+'/cs3243project/kingOfTheHill/mypoker/StudentAgentUploads/{}Player.{}'
def handle_uploaded_file(file, request):
    correct_format, message = test_file_format(file)
    user = request.user
    if correct_format:
        path = src.format(user.username,"py")
        with open(path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        user.profile.num_sub += 1
        user.profile.last_submission = datetime.datetime.today()
        user.profile.status = "Being verified."
        user.save()
        run_test_tournament(user.id)
        return render(request, 'upload.html', {'form': UploadFileForm(),
                                               'status': user.profile.status,
                                               'last_sub': user.profile.last_submission,
                                               "haveMessage": True,
                                               "messageTitle": "Success",
                                               "message": "Successfully uploaded"})
    else:
        return render(request, 'upload.html', {'form': UploadFileForm(),
                                               'status': user.profile.status,
                                               'last_sub': user.profile.last_submission,
                                               "haveMessage": True,
                                               "messageTitle": "Warning",
                                               "message": message})

add_dst1 = home+'/cs3243project/kingOfTheHill/mypoker/StudentAgentUploadsTemp/{}'
add_dst2 = home+'/cs3243project/kingOfTheHill/mypoker/StudentAgentUploads/{}'
def handle_uploaded_additional_file(file, request):
    user = request.user
    correct_format, message = test_additional_file_format(file,user.username)
    if correct_format:
        for add_dst in [add_dst1, add_dst2]:
            path = add_dst.format(file.name)
            with open(path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        try:
            upload = GroupUpload.objects.get(name=file.name)
        except GroupUpload.DoesNotExist:
            upload = GroupUpload()
        upload.user_id = user
        upload.name = file.name
        upload.time = datetime.datetime.now()
        upload.save()
        user_uploads = user.uploads.all().order_by('id')
        return render(request, 'uploadAdditional.html', {'form': UploadFileForm(),
                                                         'status': user.profile.status,
                                                         'uploads': user_uploads,
                                                         "haveMessage": True,
                                                         "messageTitle": "Success",
                                                         "message": "Successfully uploaded"})
    else:
        user_uploads = user.uploads.all().order_by('id')
        return render(request, 'uploadAdditional.html', {'form': UploadFileForm(),
                                               'status': user.profile.status,
                                               'uploads': user_uploads,
                                               "haveMessage": True,
                                               "messageTitle": "Warning",
                                               "message": message})



def object_delete(request, object_id):
    user = request.user
    upload = GroupUpload.objects.get(pk=object_id)
    if user == upload.user_id:
        upload_name = upload.name
        if os.path.exists(add_dst1.format(upload_name)):
            os.remove(add_dst1.format(upload_name))
        if os.path.exists(add_dst2.format(upload_name)):
            os.remove(add_dst2.format(upload_name))
        upload.delete()
    return redirect('/upload/')

@background(schedule=5)
def run_test_tournament(user_id):
    user = User.objects.get(pk=user_id)
    try:
        mypoker.tournaments.run_test_tournament(user.username)
    except Exception as e:
        exc_info = sys.exc_info()
        user.profile.status = str(e) + str(exc_info)
        print(exc_info)
        print(e)
    else:
        copyfile(src.format(user.username,"py"),dst.format(user.username,'py'))
        user.profile.status = "Verified!"
    if os.path.exists(dst.format(user.username,'pyc')):
        os.remove(dst.format(user.username, 'pyc'))
    if os.path.exists(src.format(user.username, 'pyc')):
        os.remove(src.format(user.username, 'pyc'))
    user.save()



def test_file_format(file):
    if file.size > 5e+8:
        return False, "Your file seems to be larger than 500 megabytes. Please upload a smaller file."
    elif not file.name.endswith('.py'):
        return False, "Your file doesn't seem to be a Python file (.py). Please submit a python file."
    return True, "Your file was successfully uploaded."

def test_additional_file_format(file,name):
    if file.size > 5e+8:
        return False, "Your file seems to be larger than 500 megabytes. Please upload a smaller file."
    elif not file.name.startswith(name):
        return False, "Your file doesn't start with your group name."
    return True, "Your file was successfully uploaded."


def save_new_king(file):
    with open(currentKingPath, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

