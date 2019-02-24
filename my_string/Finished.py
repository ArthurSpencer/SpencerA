class stri():
    
    def __init__(self, string):
        self.string = string
    #enddef
        
    def uppercase(self):
        binaryholder = list(self.string)
        for counter in range (0, len(self.string)):
            letter = ord(binaryholder[counter])
            if letter > 96:
                binaryholder[counter] = chr(letter - 32)
            #endif
        #next
        self.string = (binaryholder)
    #enddef
    
    def lowercase(self):
        binaryholder = list(self.string)
        for counter in range (0, len(self.string)):
            letter = ord(binaryholder[counter])
            if letter < 91 and letter > 64:
                binaryholder[counter] = chr(letter + 32)
            #endif
        #next
        self.string = (binaryholder)
    #enddef

    def get_string(self):
        return "".join(self.string)
    #enddef

    def set_string(self, new):
        self.string = new
    #enddef

    def set_char(self, position, char):
        self.string[position] = char
    #enddef

string1 = stri("UfDSd")
string1.lowercase()
print (string1.get_string())
string1.set_char(1,"o")
string1.uppercase()
print (string1.get_string())

        
    
