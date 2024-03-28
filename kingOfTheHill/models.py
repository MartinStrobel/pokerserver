# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


# Create your models here.
class King(models.Model):
    name = models.CharField(max_length=120)
    coronation = models.DateTimeField()


class Tournament(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField(null=True)
    tournament_id = models.AutoField(primary_key=True)

class Setting(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField(null=True)
    tournament_id = models.AutoField(primary_key=True)
    num_game = models.IntegerField(default=1)
    max_round = models.IntegerField(default=1000)
    initial_stack = models.IntegerField(default=10000)
    smallblind_amount = models.IntegerField(default=20)

class TournamentFight(models.Model):
    tournament_id = models.ForeignKey(Tournament, related_name='fights')
    player1 = models.CharField(max_length=120)
    player2 = models.CharField(max_length=120)
    player1_pot = models.IntegerField(default=-1)
    player2_pot = models.IntegerField(default=-1)
    level = models.IntegerField(default=-1)
    winner = models.CharField(null=True, max_length=120)
    margin = models.IntegerField(null=True, default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    num_sub = models.IntegerField(default=0)
    status = models.TextField(default="")
    ranking = models.IntegerField(null=True, default=-1)
    last_submission = models.DateField(null=True, blank=True)

class GroupUpload(models.Model):
    user_id = models.ForeignKey(User, related_name='uploads')
    name = models.TextField(max_length=500, blank=True)
    time = models.DateTimeField(null=True, blank=True)


class FinalTournamentResult(models.Model):
    outcome    = models.CharField(max_length=120)
    winner_id  = models.ForeignKey(User, related_name='wins',null=True, )
    loser_id   = models.ForeignKey(User, related_name='losses',null=True, )
    profit     = models.IntegerField(null=True, default=0)


class Final2TournamentResult(models.Model):
    outcome    = models.CharField(max_length=120)
    winner_id  = models.ForeignKey(User, related_name='wins2',null=True, )
    loser_id   = models.ForeignKey(User, related_name='losses2',null=True, )
    profit     = models.IntegerField(null=True, default=0)

class FinalTournament(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField(null=True)
    tournament_id = models.AutoField(primary_key=True)

class FinalTournamentFight(models.Model):
    outcome    = models.CharField(max_length=120)
    player1    = models.ForeignKey(User, related_name='finalFights1')
    player2    = models.ForeignKey(User, related_name='finalFights2')
    winner     = models.CharField(null=True, max_length=120)
    reward     = models.IntegerField(null=True, default=0)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
