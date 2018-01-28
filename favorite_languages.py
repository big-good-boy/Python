# -*- coding: utf-8 -*-

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("\tHi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following language have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

participants = ['andrew', 'john', 'phil', 'erin', 'edward']

for participant in participants:
    if participant in favorite_languages:
        print(participant.title() + ", благодарим Вас за участие в опросе")
    else:
        print(participant.title() + ", не могли бы Вы принять участие в опросе")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " + str(languages[0]).title())
    else:

        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())