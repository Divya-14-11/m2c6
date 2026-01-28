class square:
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f"THE AREA OF SQUARE IS {self.side*self.side}")
class rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def area(self):
        print(f"THE AREA OF RECTANGLE IS {self.length*self.bredth}")
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"THE AREA OF CIRCLE IS {3.14*self.radius*self.radius}")
object1=square(10)
object2=rectangle(10,10)
object3=circle(10)
for shape in (object1,object2,object3):
    shape.area()