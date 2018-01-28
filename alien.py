# -*- coding: utf-8 -*-

alien_0 = {'color': 'gren', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: "  + str(alien_0['x_position']))
# Пришелец перемещается вправо.
# Вычисляем величину смещения на основании текущей скорости
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро.
    x_increment = 3
# Новая позиция равна сумме строй позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'color': 'gren', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)