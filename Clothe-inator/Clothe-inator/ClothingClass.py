class clothing():
    """This class contains all the functions needed to do stuff with clothing items"""
    def __init__(self, username, clothingname, clothingtypekey, temprangemin, temprangemax):
        self.username = username
        self.clothingname = clothingname
        self.bodycat = bodycat
        self.temprangemin = temprangemin
        self.temprangemax = temprangemax

    def getUsername(self):
        return self.username
    #endfunction

    def getClothingName(self):
        return self.clothingname
    #endfunction

    def getClothingTypeKey(self):
        return self.clothingtypekey
    #endfunction

    def getTempRangeMin(self):
        return self.temprangemin
    #endfunction

    def getTempRangeMax(self):
        return self.temprangemax
    #endfunction

    def setClothingName(self, clothingname):
        pass
    # go to updater()
    #endprocedure

    def setClothingTypeKey(self, clothingname):
       pass
   #go to updater()
   #endprocedure

    def delete():
        pass
    #need to return to clothingdetails()
    #endprocedure 

    def updater(self,field, newvalue):
        pass
    
    #Take self.clothingname
    #-- field to update will be taken from whether it comes from setClothingName or setClothingTypeKey 
    #-- new value will be what the user entered
    #-- Update fieldtoupdate where username = self.username with new value 
    
    #endprocedure
    

    ##NOTE TO SELF - MIGHT HAVE TO REFRESH/REDO CLASS VALUES EACH TIME TO MAKE SURE IT DOESNT HAVE THE WRONG VALUES 
