# -*- coding: utf-8 -*-

places = input("Сколько мест вы хотите забронировать? ")
if int(places) < 9:
    print("Ваш стол готов")
else:
    print("Вам придётся подождать")