numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if 1 == number:
        print(str(number) + "st")
    elif 2 == number:
        print(str(number) + "nd")
    elif 3 == number:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")