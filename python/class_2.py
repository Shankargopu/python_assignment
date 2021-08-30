class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    def get_color(self):
        return self.color
    def set_color(self, color):
        selfcolor = color
class Rectangle(Shape):
    def __init__(self, length, color):
       
        self.length = length
        self.color=color
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def get_color(self):
        return self.color
class Circle(Shape):
    def __init__(self, radius,color):
        self.radius = radius
        self.color=color
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
    def set_color(self):
        return self.color
class child(Rectangle,Circle):
     def __init__(self,color,area,p):
         
         self.color=color
         self.area=area
         self.p=p
     def set_color(self):
        return self.color
     def area(self):
         return area*p   
         



obc=child('blue',50,21)
print(obc.set_color())

ob=Circle(23,'green')
print(ob.set_color())


obr=Rectangle(50,'white')
print(obr.get_color())
