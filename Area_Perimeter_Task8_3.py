#3 From the given List create two class Methods Area and Perimeter which will be going to calculate the Area and Perimeter
class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2 * 3.141
    def perimeter(self):
        return 2 * self.radius * 3.141

NewCircle = Circle(7)
print("Area:", NewCircle.area())
print("Perimeter:", NewCircle.perimeter())