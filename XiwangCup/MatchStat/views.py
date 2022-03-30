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


def goal_list(request):
    results = list(Player.objects.order_by('-goal').values('player_name', 'team', 'goal'))
    name1 = results[0]['player_name']
    goal1 = results[0]['goal']

    name2 = results[1]['player_name']
    goal2 = results[1]['goal']

    name3 = results[2]['player_name']
    goal3 = results[2]['goal']

    name4 = results[3]['player_name']
    goal4 = results[3]['goal']

    name5 = results[4]['player_name']
    goal5 = results[4]['goal']

    goal_list_return = {'name1': name1, 'goal1': goal1, 'name2': name2, 'goal2': goal2, 'name3': name3, 'goal3': goal3,
                        'name4': name4, 'goal4': goal4, 'name5': name5, 'goal5': goal5}

    return render(request, "goal_list.html", locals())
