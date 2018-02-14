# -*- coding: utf-8 -*-

# Сохрание информации о заказанной пице
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# Описание заказа
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#     "with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)

# def make_pizza(*toppings):
#     """Вывод списка заказанных дополнений."""
#     print(toppings)

def make_pizza(*toppings):
    """Вывод списка заказанных дополнений."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('popperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')