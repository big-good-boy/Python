from random import randint

class Die():
  def __init__(self, sides=6):
    self.sides = sides

  def roll_die(self):
    return(randint(1, self.sides))

cub6 = Die()
x = 1
while x < 10:
  print(cub6.roll_die())
  x += 1

cub6 = Die(10)
x = 1
while x < 10:
  print(cub6.roll_die())
  x += 1

cub6 = Die(20)
x = 1
while x < 10:
  print(cub6.roll_die())
  x += 1