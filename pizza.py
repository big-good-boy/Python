# -*- coding: utf-8 -*-

# Сохрание информации о заказанной пице
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Описание заказа
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)