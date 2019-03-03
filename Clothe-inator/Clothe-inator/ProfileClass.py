class profile():
    """When the choose account function is done, the account detail/obect will become the one chosen 
    and its attributes will contain all those in the table for that profile
    This class contains all the functions needed to do stuff with the profile"""
    def __init__(self, username, email, emailtime, algtype):
        self.username = username
        self.email = email
        self.emailtime = emailtime
        self.algtype = algtype
    #endprocedure
    
    def getUsername(self):
        return self.username
    #endfunction

    def getEmail(self):
        return self.email
    #endfunction

    def getEmailTime(self):
        return self.emailtime
    #endfunction

    def getAlgType(self):
        return self.algtype
    #endfunction 

    def setUsername(self, username):
        pass
    # go to updater()
    #endprocedure

    def setEmail(self, email):
        pass
    # go to updater()
    #endprocedure

    def setEmailTime(self, emailtime):
        pass
    # go to updater()
    #endprocedure

    def setAlgType(self, algtype):
        pass
    # go to updater()
    #endprocedure

    def deleteself(self):
        pass
    #need to return to start()
    #endprocedure

    def updater(self, field, newvalue):
        pass
    
    #Use same principal from clothing with un, em, emt and algt all pointing to updater
    #endprocedure 

#endclass


