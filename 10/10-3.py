filename = 'guest.txt'

user = input()

with open(filename, 'w') as string:
  string.write(user)