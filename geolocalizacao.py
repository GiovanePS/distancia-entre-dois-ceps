from geopy.geocoders import Nominatim
import geopy.distance

def get_location(bairro_cidade: str):
  locator = Nominatim(user_agent="localizacao")
  location = locator.geocode(bairro_cidade)
  return (location.latitude, location.longitude)


def get_distance(coordA: tuple, coordB: tuple):
  return round(geopy.distance.distance(coordA, coordB).km,2)
