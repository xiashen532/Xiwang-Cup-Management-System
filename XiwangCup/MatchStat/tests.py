from django.test import TestCase

# Create your tests here.

from models import Player, Match, Team

def goal_list_test():
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

    goal_list_return = {'name1':name1,'goal1':goal1, 'name2':name2,'goal2':goal2, 'name3':name3,'goal3':goal3, 'name4':name4,'goal4':goal4, 'name5':name5,'goal5':goal5}
    print(goal_list_return)
    print(results)
