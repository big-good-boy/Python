class Restaurant():

  def __init__(self, restaurant_name, restaurant_type, number_served=0):
    self.restaurant_name = restaurant_name.title()
    self.restaurant_type = restaurant_type
    self.number_served = number_served

  def set_number_served(self, visitors_served):
    self.number_served = visitors_served

  def increment_number_served(self, increment):
    self.number_served += increment

restaurant = Restaurant('pam', 'pam')

print(restaurant.number_served)

restaurant.number_served = 5
print(restaurant.number_served)

restaurant.set_number_served(7)
print(restaurant.number_served)

restaurant.increment_number_served(13)
print(restaurant.number_served)