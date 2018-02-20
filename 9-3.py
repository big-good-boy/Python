class User():
  def __init__(self, first_name, last_name, age_user='unknown', city_user='unknown'):
    self.first = first_name.title()
    self.last = last_name.title()
    self.age = age_user
    self.city = city_user.title()
    self.full_name = first_name.title() + " " + last_name.title()

  def describe_user(self):
    print("\nName: " + self.first + " " + self.last +
          "\nage: " + str(self.age) +
          "\ncity: " + self.city)

  def greet_user(self):
    print("Hi, " + self.full_name)

bond = User("Jamas", "Bond", 40, "london")
bond.describe_user()
bond.greet_user()

jimmi = User("jimmi", "hendrix")
jimmi.describe_user()
jimmi.greet_user()