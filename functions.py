import numpy as np
import math
#from Location import Location

def get_random_location():
  return [np.random.uniform(-90, 90), np.random.uniform(-180, 180)]

def get_distance_between_two_locations(location1, location2):
  """
  To get the distance between two locations. We use the 'haversine' formula to calculate the great-circle distance between two points. Returns the value in KM
  """
  R = 6371e3 #Radius of the earth on meters
  l1 = math.radians(location1.latitude)
  l2 = math.radians(location2.latitude)
  dif_lat = math.radians(location2.latitude - location1.latitude)
  dif_long = math.radians(location2.longitude - location1.longitude)

  a = ((math.sin(dif_lat/2) * math.sin(dif_lat/2)) +
      (math.cos(l1) * math.cos(l2)) *
      (math.sin(dif_long/2) * math.sin(dif_long/2)))

  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = R * c
  d = d / 1000 #Convert meters to kilometers

  #print(str(d) + " KM")
  #print("Rounded:",str(d),"KM")
  return round(d)
"""
mexico = Location(getRandomLocation())
usa = Location(getRandomLocation())
print("Mexico location:", mexico.location)
print("USA location:", usa.location)
print("Distance between two points:", get_distance_2_locations(mexico, usa))
"""