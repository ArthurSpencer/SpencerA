class Dog():

    def __init__(self, myName, myColour):
        self.p_name = myName
        self.p_colour = myColour
        
    def bark(self, barkTimes):
        for n in range (barkTimes):
            print("Woof!")
        #next
    #endfunction
                
            
    def setColour(self,myColour):
        self.p_colour = myColour
    #endprocedure

        
    def getColour(self):
        return self.p_colour
    #endfunction

        
    def getName(self):
        return self.p_name
    #endfunction
    
    def printDogDetails(self):
        print (self.p_name, self.p_colour)
    #endfunction

#end class

myDog3 = Dog("Mutt", "Unknown")
myDog2 = Dog("Jeff", "Unknown")


if myDog2.getColour() == "Unknown":
    print("Enter colour for ", myDog2.getName())
    newColour = input() 
    myDog2.setColour (newColour)
print(myDog2.getName(), "is", myDog2.getColour())

class Puppy(Dog):
    p_ShoesChewed = 0    
    def ShoesChewed(self, numShoes):
        self.p_ShoesChewed = p_ShoesChewed + numShoes
    #endprocedure
    def getShoesChewed(self):
        return self.p_ShoesChewed
    #endfunction
#endclass
    
myPuppy1 = Puppy("Clifford", "Red")
print (myPuppy1.getName(), "has chewed", myPuppy1.getShoesChewed(), "shoes")
