# -*- coding: utf-8 -*-

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("\nHello, " + name + "!")

# age = int(input("How old are you? "))
# print(age <= 59)

# def greet_user():
#     """Выводит простое приветствие"""
#     print("Hello!")

# greet_user()

# def greet_user(username):
#     """Выводит простое приветствие"""
#     print("Hello, " + username.title() + "!")

# greet_user('jesse')

# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# Бесконечный цикл
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")