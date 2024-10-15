class Rectangle:

    def __init__(self, height, width):
        print(f"Rectangle created with height: {height} and width {width}")
        self.height = height
        self.width = width

    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)
    
# Creating object

a = Rectangle(4, 7)
b = Rectangle(5, 8)
c = Rectangle(2, 5)

# #a.set_dimensions(4, 5)
# print("Height and width == ", a.height, a.width)
# print("Area:", a.area())
# print("Perimeter: ", a.perimeter())
