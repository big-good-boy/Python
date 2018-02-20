class Restaurant():

  def __init__(self, restaurant_name, restaurant_type):
    self.restaurant_name = restaurant_name.title()
    self.restaurant_type = restaurant_type

  def describe_restaurant(self):
    print("\n" + self.restaurant_name)
    print(self.restaurant_type)

  def open_restaurant(self):
    print("\nРесторан " + self.restaurant_name + " открыт")

class IceCreamStand(Restaurant):
  def __init__(self, restaurant_name, restaurant_type):
    super().__init__(restaurant_name, restaurant_type)

    self.flavors = ['sort1', 'sort2', 'sort3']

  def output_sort(self):
    for flovor in self.flavors:
      print(flovor)

vernisage = IceCreamStand('vernisage', 'lite')
vernisage.output_sort()