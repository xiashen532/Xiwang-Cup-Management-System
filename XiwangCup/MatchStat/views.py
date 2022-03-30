from django.shortcuts import render
from .models import Player, Match, Team


# Create your views here.

def table(request):
    groupa = Team.objects.filter(group="A")
    groupb = Team.objects.filter(group="B")
    groupc = Team.objects.filter(group="C")
    resultsa = list(groupa.order_by('-points').values('team_name', 'win', 'draw', 'lost', 'logo_url', 'points'))
    resultsb = list(groupb.order_by('-points').values('team_name', 'win', 'draw', 'lost', 'logo_url', 'points'))
    resultsc = list(groupc.order_by('-points').values('team_name', 'win', 'draw', 'lost', 'logo_url', 'points'))

    table_return_a = [
        {'team_name': resultsa[0]['team_name'], 'points': resultsa[0]['points'], 'win': resultsa[0]['win'],
         'draw': resultsa[0]['draw'], 'lost': resultsa[0]['lost'], 'logo_url': resultsa[0]['logo_url'],
         'match': resultsa[0]['win'] + resultsa[0]['draw'] + resultsa[0]['lost']},
        {'team_name': resultsa[1]['team_name'], 'points': resultsa[1]['points'], 'win': resultsa[1]['win'],
         'draw': resultsa[1]['draw'], 'lost': resultsa[1]['lost'], 'logo_url': resultsa[1]['logo_url'],
         'match': resultsa[1]['win'] + resultsa[1]['draw'] + resultsa[1]['lost']},
        {'team_name': resultsa[2]['team_name'], 'points': resultsa[2]['points'], 'win': resultsa[2]['win'],
         'draw': resultsa[2]['draw'], 'lost': resultsa[2]['lost'], 'logo_url': resultsa[2]['logo_url'],
         'match': resultsa[2]['win'] + resultsa[2]['draw'] + resultsa[2]['lost']},
        {'team_name': resultsa[3]['team_name'], 'points': resultsa[3]['points'], 'win': resultsa[3]['win'],
         'draw': resultsa[3]['draw'], 'lost': resultsa[3]['lost'], 'logo_url': resultsa[3]['logo_url'],
         'match': resultsa[3]['win'] + resultsa[3]['draw'] + resultsa[3]['lost']},
        {'team_name': resultsa[4]['team_name'], 'points': resultsa[4]['points'], 'win': resultsa[4]['win'],
         'draw': resultsa[4]['draw'], 'lost': resultsa[4]['lost'], 'logo_url': resultsa[4]['logo_url'],
         'match': resultsa[4]['win'] + resultsa[4]['draw'] + resultsa[4]['lost']},
        {'team_name': resultsa[5]['team_name'], 'points': resultsa[5]['points'], 'win': resultsa[5]['win'],
         'draw': resultsa[5]['draw'], 'lost': resultsa[5]['lost'], 'logo_url': resultsa[5]['logo_url'],
         'match': resultsa[5]['win'] + resultsa[5]['draw'] + resultsa[5]['lost']},
    ]

    table_return_b = [
        {'team_name': resultsb[0]['team_name'], 'points': resultsb[0]['points'], 'win': resultsb[0]['win'],
         'draw': resultsb[0]['draw'], 'lost': resultsb[0]['lost'], 'logo_url': resultsb[0]['logo_url'],
         'match': resultsb[0]['win'] + resultsb[0]['draw'] + resultsb[0]['lost']},
        {'team_name': resultsb[1]['team_name'], 'points': resultsb[1]['points'], 'win': resultsb[1]['win'],
         'draw': resultsb[1]['draw'], 'lost': resultsb[1]['lost'], 'logo_url': resultsb[1]['logo_url'],
         'match': resultsb[1]['win'] + resultsb[1]['draw'] + resultsb[1]['lost']},
        {'team_name': resultsb[2]['team_name'], 'points': resultsb[2]['points'], 'win': resultsb[2]['win'],
         'draw': resultsb[2]['draw'], 'lost': resultsb[2]['lost'], 'logo_url': resultsb[2]['logo_url'],
         'match': resultsb[2]['win'] + resultsb[2]['draw'] + resultsb[2]['lost']},
        {'team_name': resultsb[3]['team_name'], 'points': resultsb[3]['points'], 'win': resultsb[3]['win'],
         'draw': resultsb[3]['draw'], 'lost': resultsb[3]['lost'], 'logo_url': resultsb[3]['logo_url'],
         'match': resultsb[3]['win'] + resultsb[3]['draw'] + resultsb[3]['lost']},
        {'team_name': resultsb[4]['team_name'], 'points': resultsb[4]['points'], 'win': resultsb[4]['win'],
         'draw': resultsb[4]['draw'], 'lost': resultsb[4]['lost'], 'logo_url': resultsb[4]['logo_url'],
         'match': resultsb[4]['win'] + resultsb[4]['draw'] + resultsb[4]['lost']},
        {'team_name': resultsb[5]['team_name'], 'points': resultsb[5]['points'], 'win': resultsb[5]['win'],
         'draw': resultsb[5]['draw'], 'lost': resultsb[5]['lost'], 'logo_url': resultsb[5]['logo_url'],
         'match': resultsb[5]['win'] + resultsb[5]['draw'] + resultsb[5]['lost']},
    ]

    table_return_c = [
        {'team_name': resultsc[0]['team_name'], 'points': resultsc[0]['points'], 'win': resultsc[0]['win'],
         'draw': resultsc[0]['draw'], 'lost': resultsc[0]['lost'], 'logo_url': resultsc[0]['logo_url'],
         'match': resultsc[0]['win'] + resultsc[0]['draw'] + resultsc[0]['lost']},
        {'team_name': resultsc[1]['team_name'], 'points': resultsc[1]['points'], 'win': resultsc[1]['win'],
         'draw': resultsc[1]['draw'], 'lost': resultsc[1]['lost'], 'logo_url': resultsc[1]['logo_url'],
         'match': resultsc[1]['win'] + resultsc[1]['draw'] + resultsc[1]['lost']},
        {'team_name': resultsc[2]['team_name'], 'points': resultsc[2]['points'], 'win': resultsc[2]['win'],
         'draw': resultsc[2]['draw'], 'lost': resultsc[2]['lost'], 'logo_url': resultsc[2]['logo_url'],
         'match': resultsc[2]['win'] + resultsc[2]['draw'] + resultsc[2]['lost']},
        {'team_name': resultsc[3]['team_name'], 'points': resultsc[3]['points'], 'win': resultsc[3]['win'],
         'draw': resultsc[3]['draw'], 'lost': resultsc[3]['lost'], 'logo_url': resultsc[3]['logo_url'],
         'match': resultsc[3]['win'] + resultsc[3]['draw'] + resultsc[3]['lost']},
        {'team_name': resultsc[4]['team_name'], 'points': resultsc[4]['points'], 'win': resultsc[4]['win'],
         'draw': resultsc[4]['draw'], 'lost': resultsc[4]['lost'], 'logo_url': resultsc[4]['logo_url'],
         'match': resultsc[4]['win'] + resultsc[4]['draw'] + resultsc[4]['lost']},
        {'team_name': resultsc[5]['team_name'], 'points': resultsc[5]['points'], 'win': resultsc[5]['win'],
         'draw': resultsc[5]['draw'], 'lost': resultsc[5]['lost'], 'logo_url': resultsc[5]['logo_url'],
         'match': resultsc[5]['win'] + resultsc[5]['draw'] + resultsc[5]['lost']},
    ]

    return render(request, "table.html", locals())


def id_to_team_name(num):
    res = Team.objects.filter(id=num)
    rtn = res[0].team_name
    return rtn


def id_to_logo_url(num):
    res = Team.objects.filter(id=num)
    rtn = res[0].logo_url
    return rtn


def stats(request):
    ordergoal = list(Player.objects.order_by('-goal').values('player_name', 'player_team', 'goal', 'photo_url'))
    orderycard = list(Player.objects.order_by('-y_card').values('player_name', 'player_team', 'y_card', 'photo_url'))
    orderrcard = list(Player.objects.order_by('-r_card').values('player_name', 'player_team', 'r_card', 'photo_url'))

    resultsgoal = [
        {'player_name': ordergoal[0]['player_name'], 'player_team': id_to_team_name(ordergoal[0]['player_team']),
         'goal': ordergoal[0]['goal'],
         'photo_url': ordergoal[0]['photo_url'],
         'logo_url': id_to_logo_url(ordergoal[0]['player_team']),
         },
        {'player_name': ordergoal[1]['player_name'], 'player_team': id_to_team_name(ordergoal[1]['player_team']),
         'goal': ordergoal[1]['goal'],
         'photo_url': ordergoal[1]['photo_url'],
         'logo_url': id_to_logo_url(ordergoal[1]['player_team']),
         },
        {'player_name': ordergoal[2]['player_name'], 'player_team': id_to_team_name(ordergoal[2]['player_team']),
         'goal': ordergoal[2]['goal'],
         'photo_url': ordergoal[2]['photo_url'],
         'logo_url': id_to_logo_url(ordergoal[2]['player_team']),
         },
        {'player_name': ordergoal[3]['player_name'], 'player_team': id_to_team_name(ordergoal[3]['player_team']),
         'goal': ordergoal[3]['goal'],
         'photo_url': ordergoal[3]['photo_url'],
         'logo_url': id_to_logo_url(ordergoal[3]['player_team']),
         },
        {'player_name': ordergoal[4]['player_name'], 'player_team': id_to_team_name(ordergoal[4]['player_team']),
         'goal': ordergoal[4]['goal'],
         'photo_url': ordergoal[4]['photo_url'],
         'logo_url': id_to_logo_url(ordergoal[4]['player_team']),
         },
    ]

    resultsycard = [
        {'player_name': orderycard[0]['player_name'], 'player_team': id_to_team_name(orderycard[0]['player_team']),
         'y_card': orderycard[0]['y_card'],
         'photo_url': orderycard[0]['photo_url'],
         'logo_url': id_to_logo_url(orderycard[0]['player_team']), },
        {'player_name': orderycard[1]['player_name'], 'player_team': id_to_team_name(orderycard[1]['player_team']),
         'y_card': orderycard[1]['y_card'],
         'photo_url': orderycard[1]['photo_url'],
         'logo_url': id_to_logo_url(orderycard[1]['player_team']), },
        {'player_name': orderycard[2]['player_name'], 'player_team': id_to_team_name(orderycard[2]['player_team']),
         'y_card': orderycard[2]['y_card'],
         'photo_url': orderycard[2]['photo_url'],
         'logo_url': id_to_logo_url(orderycard[2]['player_team']), },
        {'player_name': orderycard[3]['player_name'], 'player_team': id_to_team_name(orderycard[3]['player_team']),
         'y_card': orderycard[3]['y_card'],
         'photo_url': orderycard[3]['photo_url'],
         'logo_url': id_to_logo_url(orderycard[3]['player_team']), },
        {'player_name': orderycard[4]['player_name'], 'player_team': id_to_team_name(orderycard[4]['player_team']),
         'y_card': orderycard[4]['y_card'],
         'photo_url': orderycard[4]['photo_url'],
         'logo_url': id_to_logo_url(orderycard[4]['player_team']), },
    ]

    resultsrcard = [
        {'player_name': orderrcard[0]['player_name'], 'player_team': id_to_team_name(orderrcard[0]['player_team']),
         'r_card': orderrcard[0]['r_card'],
         'photo_url': orderrcard[0]['photo_url'],
         'logo_url': id_to_logo_url(orderrcard[0]['player_team']), },
        {'player_name': orderrcard[1]['player_name'], 'player_team': id_to_team_name(orderrcard[1]['player_team']),
         'r_card': orderrcard[1]['r_card'],
         'photo_url': orderrcard[1]['photo_url'],
         'logo_url': id_to_logo_url(orderrcard[1]['player_team']), },
        {'player_name': orderrcard[2]['player_name'], 'player_team': id_to_team_name(orderrcard[2]['player_team']),
         'r_card': orderrcard[2]['r_card'],
         'photo_url': orderrcard[2]['photo_url'],
         'logo_url': id_to_logo_url(orderrcard[2]['player_team']), },
        {'player_name': orderrcard[3]['player_name'], 'player_team': id_to_team_name(orderrcard[3]['player_team']),
         'r_card': orderrcard[3]['r_card'],
         'photo_url': orderrcard[3]['photo_url'],
         'logo_url': id_to_logo_url(orderrcard[3]['player_team']), },
        {'player_name': orderrcard[4]['player_name'], 'player_team': id_to_team_name(orderrcard[4]['player_team']),
         'r_card': orderrcard[4]['r_card'],
         'photo_url': orderrcard[4]['photo_url'],
         'logo_url': id_to_logo_url(orderrcard[4]['player_team']), },
    ]

    return render(request, "stats.html", locals())

