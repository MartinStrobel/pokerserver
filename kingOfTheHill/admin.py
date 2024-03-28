# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import King, Profile, Tournament, TournamentFight, Setting, GroupUpload, FinalTournamentResult, Final2TournamentResult

admin.site.register(GroupUpload)
admin.site.register(King)
admin.site.register(Profile)
admin.site.register(Tournament)
admin.site.register(TournamentFight)
admin.site.register(Setting)
admin.site.register(FinalTournamentResult)
admin.site.register(Final2TournamentResult)
