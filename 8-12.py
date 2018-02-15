# -*- coding: utf-8 -*-

# def list_components(*components):
#     print("\nСписок компонентов:")
#     for component in components:
#         print(component)

# list_components('Помидор')
# list_components('Помидор', 'Колбаса', 'Огурец')



# def build_profile(first, last, **user_info):
#     """Строит словарь с информацией о пользователи"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('albert', 'einstein',
#                              location='princetin',
#                              field='physics')

# build_profile = build_profile('james', 'bond',
#                               color='black',
#                               weapons='walter',
#                               car='ferrari')

# print(user_profile)
# print(build_profile)

def make_car(brand, model, **info_car):
    auto = {}
    auto['brand_auto'] = brand
    auto['model_auto'] = model
    for key, value in info_car.items():
        auto[key] = value
    return auto

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)