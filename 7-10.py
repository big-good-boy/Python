responses = {}

polling_active = True

while polling_active:
  name = input("Как вас зовут: ")
  place = input("Где вы хотели бы отдыхать? ")

  responses[name] = place

  repeat = input("Повторить опрос? ")
  if repeat == 'no':
    polling_active = False

print("\n--- Опрос завершён ---")
for name, place in responses.items():
  print(name.title() + " хочет отдыхать в " + place)