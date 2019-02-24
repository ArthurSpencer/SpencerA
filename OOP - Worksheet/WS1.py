class Dog():

    def __init__(self, myName, myColour):
        self.p_name = myName
        self.p_colour = myColour
    #enddef        
    def bark(self, barkTimes):
        for n in range (barkTimes):
            print("Woof!")
    #enddef           
    def setColour(self,myColour):
        self.p_colour = myColour
    #enddef        
    def getColour(self):
        return self.p_colour
    #enddef        
    def getName(self):
        return self.p_name
    #enddef    
    def printDogDetails(self):
        print (self.p_name, self.p_colour)
    #enddef
#end class

myDog3 = Dog("Mutt", "Unknown")
myDog2 = Dog("Jeff", "Unknown")

if myDog2.getColour() == "Unknown":
    print("Enter colour for ", myDog2.getName())
    newColour = input() 
    myDog2.setColour (newColour)
#endif
print(myDog2.getName(), "is", myDog2.getColour())
