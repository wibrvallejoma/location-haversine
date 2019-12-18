class Location:
  """A location from Earth. We are storing the location([latitude, longitude])."""

  def __init__(self, location):
    if type(location) not in [list]:
      raise ValueError("The location must be a list with two values [latitude, longitude].")

    if len(location) != 2:
      raise ValueError("The location must be a list with two values [latitude, longitude].")

    if type(location[0]) not in [int, float]:
      raise ValueError("The latitude must be a real number.")

    if type(location[-1]) not in [int, float]:
      raise ValueError("The longitude must be a real number.")

    if location[0] > 90 or location[0] < -90:
      raise ValueError("The latitude cannot be more than 90 or less than -90.")

    if location[-1] > 180 or location[-1] < -180:
      raise ValueError("The longitude cannot be more than 180 or less than -180.")

    # Extract latitude and longitude from location
    self.latitude = location[0]  #-90(S) to 90(N)
    self.longitude = location[-1] #-180(W) to 180(E)

    self.location = [self.get_latitude(), self.get_longitude()]

  def get_latitude(self):
    """Return the latitude of the Location in decimal degrees format."""
    return str(self.latitude) + " N" if self.latitude >= 0 else str(self.latitude * -1) + " S"

  def get_longitude(self):
    """Return the longitude of the Location in decimal degrees format."""
    return str(self.longitude) + " E" if self.longitude >= 0 else str(self.longitude * -1) + " W"