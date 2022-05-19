# class example
class Cuboid:
    name = "Cuboid"  # class attribute

    def __init__(self, length, breadth, height, weight):
        self.length = length  # instance attribute
        self.breadth = breadth  # instance attribute
        self.height = height  # instance attribute
        self.weight = weight  # instance attribute

    def volume(self):
        x = self.length
        y = self.breadth
        z = self.height
        v = x * y * z
        print("The volume is:", v)

    def density(self):
        x = self.length
        z = self.height
        y = self.breadth
        v = x * y * z
        d = self.weight / v
        print("Density is:", d)

    def surface_area(self):
        x = self.length
        y = self.breadth
        z = self.height
        s = 2 * (x * y + y * z + x * z)
        print("The surface area is:", s)


myCuboid = Cuboid(1, 2, 4, 4.5)
myCuboid.density()
myCuboid.surface_area()
myCuboid.volume()