class profile():

    def __init__(self, username, email, emailtime):
        self.username = username
        self.email = email
        self.emailtime = emailtime
    
    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def getEmailtime(self):
        return self.emailtime

class clothing():

    def __init__(self, username, clothingname, bodycat, warmth):
        self.username = username
        self.clothingname = clothingname
        self.bodycat = bodycat
        self.warmth = warmth 

