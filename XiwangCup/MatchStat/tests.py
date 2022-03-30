from django.test import TestCase

# Create your tests here.
from models import Player, Match, Team


def table():
    groupa = Team.objects.filter(group="a")
    groupb = Team.objects.filter(group="b")
    groupc = Team.objects.filter(group="c")
    resultsa = list(groupa.order_by('-points').values('team_name', 'win', 'draw', 'lost', 'logo_url'))
    resultsb = list(groupb.order_by('-points').values('team_name', 'win', 'draw', 'lost', 'logo_url'))
    resultsc = list(groupc.order_by('-points').values('team_name', 'win', 'draw', 'lost', 'logo_url'))
    print(resultsa)
    print(groupa)
    return
