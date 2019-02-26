
class Shape():
    def __init__(self, myColourFill, myColourOutline):
        self.colourFill = myColourFill
        self.colourOutline = myColourOutline
    #enddef
    
    def calculateArea(self, mySide):  # This is a procedure, so it should have end procedure
        self.area = mySide * mySide      
    #end procedure
#End Class

class Rectangle(Shape):
    def __init__(self, myColourFill, myColourOutline, myHeight,myWidth):
        self.height = myHeight
        self.width = myWidth
    #enddef
        
    def calculateArea(self):
        self.area = self.height * self.width
        return self.area
    #enddef
    
class Circle(Shape):
    def __init__(self, myColourFill, myColourOutline, myRadius):
        self.radius = myRadius
    #enddef
        
    def calculateArea(self):
        self.area = 3.142 * self.radius * self.radius
        return self.area
    #enddef
    
blueRectangle = Rectangle ("Blue", "Blue",3,4)
print("Blue rectangle has area",blueRectangle.calculateArea())

redCircle = Circle ("Red", "Red", 5)
print ("Red circle has area",redCircle.calculateArea())
