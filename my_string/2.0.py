class stri():

    def __init__(self, string):
        self.string = string

    def uppercase(self):
        binaryholder = []
        binaryholder = list(self.string)
        for counter in range (0, len(self.string)):
            letter = ord(binaryholder[counter])
            if letter > 96:
                letter = letter - 32
                letter = chr(letter)
                binaryholder[counter] = letter
            #endif
        #next
        self.string = (binaryholder)
    
    def lowercase(self):
        binaryholder = []
        binaryholder = list(self.string)
        for counter in range (0, len(self.string)):
            letter = ord(binaryholder[counter])
            if letter < 91:
                letter = letter + 32
                letter = chr(letter)
                binaryholder[counter] = letter
            #endif
        #next
        self.string = (binaryholder)

    def get_string(self):
        return "".join(self.string)
    #endfunction

    def set_string(self, new):
        self.string = new
    #endfunction

    def set_char(self, position, char):
        self.string[position] = char
    #endfunction

string1 = stri("uppercase")
string1.uppercase()
print (string1.get_string())

string1.set_char(1,"o")
string1.uppercase()
print (string1.get_string())
##        print(self.string)
##        binaryholder = []
##        final = ""
##        print(string)
##        binaryholder = list(string)
##        letter = ""
##        for counter in range (0, len(string)):
##            letter = binaryholder[counter]
##            letter = ord(letter)
##            if letter > 96:
##                letter = letter - 32
##                letter = chr(letter)
##                binaryholder[counter] = letter
##        #next
##        print (binaryholder)

        
    
