class Circle():
    def __init__(self,r):
        self.radius=r

    def area(self):
        return 3.14*self.radius*self.radius

    def perimeter(self):
        return 2*3.14*self.radius


print("************************************")
print("       CIRCLE CALCULATOR")
print("************************************")

newCircle=Circle(7)

print("Radius of the Circle is",newCircle.radius)
print("Area of the Circle is",newCircle.area())
print("Perimeter of the Circle is",newCircle.perimeter())

print("************************************")
print("       CALCULATION COMPLETE")
print("************************************") 