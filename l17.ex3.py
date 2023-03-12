class Vector:
    def __init__(self, x=2, y=4, z=9):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        len = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return len

    def __repr__(self):
        vector = f'{self.__class__.__name__}: ({self.x}, {self.y}, {self.z})'
        return vector

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            a = Vector((self.y * other.z) - (self.z * other.y), (self.z * other.x) - (self.x * other.z),
                       (self.x * other.y) - (self.y * other.x))
            return a
        else:
            a = Vector(self.x * other, self.y * other, self.z * other)
            return a

    def __eq__(self, other):
        if isinstance(other, Vector) and self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __pow__(self, other):
        x1 = self.x ** other
        y1 = self.y ** other
        z1 = self.z ** other
        return Vector(x1, y1, z1)