while True:
  a = input("Введите первое слогаемое ")
  b = input("Введите второе слогаемое ")
  try:
    c = int(a) + int(b)
    print("Сумма слогаемых: " + str(c) + "\n")
    break
  except ValueError:
    print("Пожалуйста, вводите числа\n")