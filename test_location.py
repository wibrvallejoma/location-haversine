import unittest
from Location import Location
from functions import get_random_location, get_distance_between_two_locations

class TestLocation(unittest.TestCase):

  def test_getLatitude(self):
    # Test the parsing of latitude from -50 to 50 S; from 30 to 30 N; etc.
    l1 = Location([50, 0])
    l2 = Location([-30, 0])
    l1_latitude = l1.get_latitude()
    l2_latitude = l2.get_latitude()
    self.assertAlmostEqual(l1_latitude, "50 N")
    self.assertAlmostEqual(l2_latitude, "30 S")

  def test_getLongitude(self):
    # Test the parsing of latitude from -100 to 100 W; from 10 to 10 E; etc.
    l1 = Location([10, -100])
    l2 = Location([10, 30])
    l1_longitude = l1.get_longitude()
    l2_longitude = l2.get_longitude()
    self.assertAlmostEqual(l1_longitude, "100 W")
    self.assertAlmostEqual(l2_longitude, "30 E")

  def test_Location(self):
    # Make sure value errors are raised when necessary
    self.assertRaises(ValueError, Location, 0)
    self.assertRaises(ValueError, Location, True)
    self.assertRaises(ValueError, Location, 1+5j)
    self.assertRaises(ValueError, Location, [])
    self.assertRaises(ValueError, Location, [0, 1, 2])
    self.assertRaises(ValueError, Location, ['hello', 0.5])
    self.assertRaises(ValueError, Location, [100, -90])
    self.assertRaises(ValueError, Location, [90, -200])

    # Test values of location [parsed latitude, parsed longitude]
    l1 = Location([-50, 125]).location
    self.assertAlmostEqual(l1, ["50 S", "125 E"])

  def test_get_random_location(self):
    # Test range of latitude and longitude
    #Latitude
    self.assertGreaterEqual(get_random_location()[0], -90)
    self.assertLessEqual(get_random_location()[0], 90)
    #Longitude
    self.assertGreaterEqual(get_random_location()[-1], -180)
    self.assertLessEqual(get_random_location()[-1], 180)

  def test_distance_between_two_locations(self):
    # Test distance when are two points at 0,0
    location1 = Location([0, 0])
    location2 = Location([0, 0])
    self.assertAlmostEqual(get_distance_between_two_locations(location1, location2), 0)

    # Test distance between two locations
    location1 = Location([54, 30])
    location2 = Location([50, -100])
    self.assertAlmostEqual(get_distance_between_two_locations(location1, location2), 7546)