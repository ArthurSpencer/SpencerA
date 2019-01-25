class Dog():

    def __init__(self, myName, myColour):
        self.p_name = myName
        self.p_colour = myColour
        
    def bark(self, barkTimes):
        for n in range (barkTimes):
            print("Woof!")
            
    def setColour(self,myColour):
        self.p_colour = myColour
        
    def getColour(self):
        return self.p_colour
        
    def getName(self):
        return self.p_name
    
    def printDogDetails(self):
        print (self.p_name, self.p_colour)

#end class

myDog3 = Dog("Mutt", "Unknown")
myDog2 = Dog("Jeff", "Unknown")

if myDog2.getColour() == "Unknown":
    print("Enter colour for ", myDog2.getName())
    newColour = input() 
    myDog2.setColour (newColour)
print(myDog2.getName(), "is", myDog2.getColour())
