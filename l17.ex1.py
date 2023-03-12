class StarSystem:
    def __init__(self, planets, name='bob'):
        self.planets = list(planets)
        self.name = name

    def __len__(self):
        return len(self.planets)

    def info(self):
        print( self.planets)
        planets_1 = self.planets.copy()
        planets_1.reverse()
        del planets_1[planets_1.index('b')]
        print(planets_1)
        for i in planets_1:
            print(i)

    def __sub__(self, other):
        planets_1 = self.planets.copy()
        planets_1.reverse()
        for i in other:
            if i in planets_1:          # WORKS
                del planets_1[planets_1.index(i)]
        planets_1.reverse
        return planets_1

    def __rsub__(self, other):
        planets_1 = self.planets.copy()  # ['1','2','3'] - a = ['1']   a = ['2','3','4']
        for i in planets_1:             # WORKS
            if i in other:
                del other[other.index(i)]
        return other

    def __isub__(self, other):
        planets_1 = self.planets.copy()   # ['1','2','3'] -= ['2','4'] =>   ['1','3']
        planets_1.reverse()
        for i in other:
            if i in planets_1:           # WORKS
                del planets_1[planets_1.index(i)]
        planets_1.reverse
        return planets_1


