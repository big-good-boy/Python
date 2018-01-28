# -*- coding: utf-8 -*-

pizza_names = ['Деревенская', 'Охотничья', 'Домашняя']

for pizza_name in pizza_names:
	print("Моя любимая пицца - " + pizza_name.lower())

print("\nА если честно, я к пицце достаточно равнодушен.\nИ накаких любимых пицц у меня нет.")

friend_pizzas = pizza_names[:]
pizza_names.append('Шашлычная')
friend_pizzas.append('Грибная')
print("\nMy favorite pizzas are:")
for pizza_name in pizza_names:
	print(pizza_name)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
