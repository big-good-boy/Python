from restaurant import Restaurant

class IceCreamStand(Restaurant):
  def __init__(self, restaurant_name, restaurant_type):
    super().__init__(restaurant_name, restaurant_type)

    self.flavors = ['sort1', 'sort2', 'sort3']

  def output_sort(self):
    for flovor in self.flavors:
      print(flovor)

vernisage = IceCreamStand('vernisage', 'lite')
vernisage.output_sort()