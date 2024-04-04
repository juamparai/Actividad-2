from package_act_1.data import *
from package_act_1.my_modules import *

team_data = generate_structure (names, goals, goals_avoided, assists)

for jugador in team_data:
    print (jugador)

topscorer = calculate_top(team_data, 1)
print (f'Goleador/a: {topscorer[0]}')


most_influential = calculate_best(team_data)
print (f'Más influyente: {most_influential}')


total_goals = sum (goals)
goals_per_match = total_goals/games_played
print (f'Se anotó un promedio de {goals_per_match} goles por partido.\n{topscorer[0]} tuvo un promedio personal de {topscorer[1]/games_played}')

