from mimetypes import init


class Cookie:

  def __init__(self, colour):
    self.colour = colour

  def get_colour(self):
    return self.colour

  def set_colour(self, colour):
    self.colour = colour

cookie_one = Cookie('blue')
cookie_two = Cookie('black')

print(f"Cookie one is ", cookie_one.get_colour())
print(f"Cookie two is ", cookie_two.get_colour())
cookie_two.set_colour('red')
print(f"Cookie two is changing colour?!?! cookie is now {cookie_two.get_colour()}")
