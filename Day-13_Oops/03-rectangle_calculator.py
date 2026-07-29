# Methods  #Return values

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Rectangle Length :", self.length)
        print("Rectangle Width  :", self.width)
        print("Area             :", self.area())
        print("Perimeter        :", self.perimeter())


# Creating Objects
r1 = Rectangle(10, 5)
r2 = Rectangle(7, 3)

print("===== Rectangle 1 =====")
r1.display()

print()

print("===== Rectangle 2 =====")
r2.display()
