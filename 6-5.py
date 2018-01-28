# -*- coding: utf-8 -*-

countries_and_rivers = {
    'волга': 'россия',
    'нил': 'египет',
    'миссисипи': 'сша',
}

for river, country in countries_and_rivers.items():
    print("Река " + river.title() + " течёт в " + country.title())

for river in countries_and_rivers.keys():
    print(river)

for country in countries_and_rivers.values():
    print(country)