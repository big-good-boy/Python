filename = 'guest.txt'

user = input("Как вас зовут: ")

with open(filename, 'a') as string:
  string.write(user + '\n')