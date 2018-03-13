def city_country(city, country, population=''):
  if population:
    full = city.title() + ", " + country.title() + " - " + population
  else:
    full = city.title() + ", " + country.title()
  return full