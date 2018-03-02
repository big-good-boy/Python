class Dog():
  """Простая модель собаки."""

  def __init__(self, name, age):
    """Инициализирует атрибуты name и age."""
    self.name = name
    self.age = age

  def sit(self):
    """Собака садится по команде."""
    print(self.name.title() + " is now setting.")
  def roll_over(self):
    """Собака перекатывается по команде."""
    print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()