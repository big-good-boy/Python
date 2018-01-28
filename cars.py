cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']

print(sorted(cars)) # ['audi', 'bmw', 'subaru', 'toyota']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse();
print(cars) # ['subaru', 'toyota', 'audi', 'bmw']

print(len(cars))

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())