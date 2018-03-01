fileName = 'answers.txt'

prompt = 'Почему вам нравится програмировать?\n'
prompt += 'для завершения работы наберите exit\n'

while True:
  string = input(prompt)
  if string != 'exit':
    with open(fileName, 'a') as file_object:
      file_object.write(string + '\n')
    continue
  else:
    break