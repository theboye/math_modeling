G = 6.67 * 10 ** (-11) 
c = 3 * 10 ** 8 

class Planet:
    count = 0
    def  __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        Planet.count = Planet.count + 1

    @staticmethod
    def diameter(radius):
        return radius * 2
    
    @classmethod
    def number(cls):
      return cls.count

    @property
    def grav_radius(self):
        print(f"grav radius is {2 * G * self.mass / (c ** 2)} м")

print(Planet.diameter(10000))
print(Planet.number())
planet1 = Planet(1000, 3 * 10 ** 20)
planet2 = Planet(25 * 10 ** 7, 2 * 10 ** 15)
print(Planet.number())
planet2.grav_radius