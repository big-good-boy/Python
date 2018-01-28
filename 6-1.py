# -*- coding: utf-8 -*-

president = {
    'first_name': 'Владимир',
    'last_name': 'Путин',
    'age': 65,
    'city': 'Москва',
}

print(president['first_name'] + " " +
    president['last_name'] + ", " +
    str(president['age']) + " лет, " +
    "город " + president['city'])

list_of_favorite_numbers = {
    'john': 7,
    'mikle': 1,
    'james': 13,
    'harry': 0,
    'mary': 9
}

for number in list_of_favorite_numbers:
    print("Любимое число " + number.title() + ": " + str(list_of_favorite_numbers[number]))

glossary = {
    'title()': 'Первая буква каждого слова - прописная, остальные - строчные',
    'upper()': 'Вся строка прописная',
    'lower()': 'Вся строка строчная',
    'rstrip()': 'Удаление пропусков в конце строки',
    'lstrip()': 'Удаление пропусков в начале строки',
}
for determination in glossary:
    print("\n" + determination + ":\n\t" + glossary[determination])

aeinsein = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': '76',
    'city': 'princeton',
}
mcurie = {
    'first_name': 'marie',
    'last_name': 'carie',
    'age': '66',
    'city': 'paris',
}
people = [president, aeinsein, mcurie]

for user in people:
    print("\n")
    for key, value in user.items():
        print(key + ": " + str(value).title())