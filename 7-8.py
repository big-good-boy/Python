# sandwich_orders = ['грибной', 'шашлычный', 'пикантный']
# finished_sandwiches = []

# while sandwich_orders:
#   i = sandwich_orders.pop()
#   print("I made your " + i + " sandwich")
#   finished_sandwiches.append(i)

# for finished_sandwiches in finished_sandwiches:
#   print(finished_sandwiches.title() + " сындвич изготовлен")

sandwich_orders = ['pastrami', 'грибной', 'pastrami', 'шашлычный', 'пикантный', 'pastrami']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
  if sandwich_order == 'pastrami':
    print("Извените, pastrami закончились")
    break

while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

while sandwich_orders:
  i = sandwich_orders.pop()
  print("I made your " + i + " sandwich")
  finished_sandwiches.append(i)

for finished_sandwiches in finished_sandwiches:
  print(finished_sandwiches.title() + " сындвич изготовлен")