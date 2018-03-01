def guest_book(filename):
  """Выводит уникальное приветствие с записью в файл с передоваемым именем"""
  prompt = 'Как к вам можно обращаться?\n'
  prompt += 'Для завершения работы нажмите Enter.\n\t'
  userName = True

  while userName:
    userName = input(prompt)
    if userName:
      message = userName.title() + ", мы рады Вас видеть у нас в гостях!\n"
      print(message)
      with open(filename, 'a') as file_object:
          file_object.write(message)
    else:
      print("До встречи")
    continue

guest_book('guest_book.txt')