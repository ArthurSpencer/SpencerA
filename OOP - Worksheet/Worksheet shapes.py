
class Shape():
    def __init__(self, myColourFill, myColourOutline):
        self.colourFill = myColourFill
        self.colourOutline = myColourOutline
    #end procedure
    
    def calculateArea(self, mySide):  # This is a procedure, so it should have end procedure
        self.area = mySide * mySide      
    #end procedure
<<<<<<< HEAD

#endclass
=======
#End Class
>>>>>>> 52a90e463522c99c7536008379b5203cb7fbfcf4

class Rectangle(Shape):
    def __init__(self, myColourFill, myColourOutline, myHeight,myWidth):
        self.height = myHeight
        self.width = myWidth
    #end procedure
        
    def calculateArea(self):
        self.area = self.height * self.width
        return self.area
    #end procedure

#endclass
    
class Circle(Shape):
    def __init__(self, myColourFill, myColourOutline, myRadius):
        self.radius = myRadius
    #end procedure
        
    def calculateArea(self):
        self.area = 3.142 * self.radius * self.radius
        return self.area
    #end procedure

#endclass
    
blueRectangle = Rectangle ("Blue", "Blue",3,4)
print("Blue rectangle has area",blueRectangle.calculateArea())

redCircle = Circle ("Red", "Red", 5)
print ("Red circle has area",redCircle.calculateArea())
