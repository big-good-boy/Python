# -*- coding: utf-8 -*-

players = ['chares', 'martina', 'michael', 'florence', 'eli']
# Срез списка
print(players[0:3]) # ['chares', 'martina', 'michael']
print(players[1:4]) # ['martina', 'michael', 'florence']
print(players[:4])  # ['chares', 'martina', 'michael', 'florence']
print(players[2:])  # ['michael', 'florence', 'eli']
print(players[-3:]) # ['michael', 'florence', 'eli']

print("Here are the first three players on my team")
for player in players[:3]:
	print(player.title())