from django import forms
from django.contrib.auth.models import User

users = User.objects.filter(username__contains="Group").order_by('username')

ALL_GROUPS = [(user.username,user.username) for user in users]

class UploadFileForm(forms.Form):
    file = forms.FileField()


class StartFinalTournamentForm(forms.Form):
    groupNumber = forms.Select(choices=ALL_GROUPS)
