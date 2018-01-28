question = "Склько вам лет? "
age = int(input(question))

if age > 0 and age < 200:
  if age < 3:
    price = 0
  elif age < 12:
    price = 10
  else:
    price = 15
  print("Цена билета " + str(price) + "$")
else:
  print("Проверьте, пожалуйста, введённые данные")