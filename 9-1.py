class Restaurant():

  def __init__(self, restaurant_name, restaurant_type):
    self.restaurant_name = restaurant_name.title()
    self.restaurant_type = restaurant_type

  def describe_restaurant(self):
    print("\n" + self.restaurant_name)
    print(self.restaurant_type)

  def open_restaurant(self):
    print("\nРесторан " + self.restaurant_name + " открыт")

cafe = Restaurant('veneciya', 'lite')

print(cafe.restaurant_name)
print(cafe.restaurant_type)

cafe.describe_restaurant()
cafe.open_restaurant()

blinnaya = Restaurant('Ural', 'elite')
blinnaya.describe_restaurant()