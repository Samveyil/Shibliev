list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

players_number = len(list_players)
first_team = list_players[:int(players_number / 2):1]
second_team = list_players[int(players_number / 2)::1]

print(first_team)
print(second_team)
