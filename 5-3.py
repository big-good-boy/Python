# -*- coding: utf-8 -*-

alien_color = 'green'
if 'green' == alien_color:
    score = 5
elif 'yellow' == alien_color:
    score = 10
elif 'red' == alien_color:
    score = 15
else:
    score = 0
    
print("Вы заработали " + str(score) +" очков")



age = 7
if age < 2:
    print("младенец")
elif age < 4:
    print("малыш")
elif age < 13:
    print("ребенок")
elif age < 20:
    print("подросток")
elif age < 65:
    print("взрослый")
elif age >= 65:
    print("пожилой человек")



fruit = ['apple', 'orange', 'pear']
if 'apple' in fruit:
    print("You realy like apple!")
if 'bananas' in fruit:
    print("You realy like bananas!")
if 'pear' in fruit:
    print("You realy like pear!")
if 'orange' in fruit:
    print("You realy like orange!")
if 'raspberry' in fruit:
    print("You realy like raspberry!")