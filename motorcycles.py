motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

motorcycles.append('honda')
print(motorcycles) # ['ducati', 'yamaha', 'suzuki', 'honda']

motorcycles.insert(0, 'bmw')
print(motorcycles) # ['bmw', 'ducati', 'yamaha', 'suzuki', 'honda']

del motorcycles[0]
print(motorcycles) # ['ducati', 'yamaha', 'suzuki', 'honda']

popped_motorcycles = motorcycles.pop()
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']
print(popped_motorcycles) # honda

too_expensive = motorcycles.remove('ducati')
print(motorcycles) # ['yamaha', 'suzuki']