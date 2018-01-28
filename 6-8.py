krosh = {
    "view": 'parrot',
    "owner's name": 'andrew',
}

reks = {
    "view": 'dog',
    "owner's name": 'police',
}

pets = [krosh, reks]

for info in pets:
    print("\n")
    for owners_name, view in info.items():
        print(owners_name + ": " + view)