class Dog():

    def __init__(self, myName, myColour):
        self.p_name = myName
        self.p_colour = myColour
    #enddef      
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
    
    def __init__(self, myName, myColour, myDob):
        super().__init__(myName, myColour)
        self.p_Dob = myDob
    #enddef        
    def ShoesChewed(self, numShoes):
        self.p_ShoesChewed = p_ShoesChewed + numShoes
    #endprocedure
    def getShoesChewed(self):
        return self.p_ShoesChewed
    #endfunction

    def printDogDetails(self):
        print (self.p_name, self.p_colour, self.p_Dob)
    #enddef
    def bark(barkTimes):
        for n in range (barkTimes):
            print("Yap")
    #enddef
    def getDob(self):
        return self.p_Dob
     #enddef       
#endclass
    
myPuppy1 = Puppy("Clifford", "Red", "12/08/2016")
print (myPuppy1.getName(), "has chewed", myPuppy1.getShoesChewed(), "shoes")
Puppy.bark(2)

myPuppy2 = Puppy("Malia", "Light Brown", "12/08/2016")

myPuppy2.printDogDetails()
