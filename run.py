from package_act_1 import *

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, Francsica, FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]
games_played = 25


team_data = generate_structure (names, goals, goals_avoided, assists)


topscorer = calculate_top(team_data, 1)
print (f'Goleador/a: {topscorer[0]}')


most_influential = calculate_best(team_data)
print (f'Más influyente: {most_influential}')


total_goals = sum (goals)
goals_per_match = total_goals/games_played
print (f'Se anotó un promedio de {goals_per_match} goles por partido.\n{topscorer[0]} tuvo un promedio personal de {topscorer[1]/games_played}')

