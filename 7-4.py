# message = "\nВведите дополнение для пиццы"
# message += "\nДля выхода наберите 'quit' "

# answer = ""

# while answer != 'quit':
#   answer = input(message)
#   if answer != 'quit':
#     print("\n" + answer + " добавлен в заказ")

message = "\nВведите дополнение для пиццы"
message += "\nДля выхода наберите 'quit' "
answer = ""
active = True

while active:
  answer = input(message)
  if answer == 'quit':
    active = False
    break
  print("\n" + answer + " добавлен в заказ")