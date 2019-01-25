import random
import binascii
import os
bin4trChar = ''

encodee = input("What message would you like to encode\n")
lengthEncodee = len(encodee)

for counter in range (lengthEncodee):

    for counter in range (8):
        Rando = (random.randint(0,1))
        if Rando < 1:
            binaryDigit = 0
        else:
            binaryDigit = 1
            

        bin4trChar = str(bin4trChar) + str(binaryDigit)
            
        #(High likelihood this doesnt matter) bin4trChar = int(bin4trChar) ALERT ALERT ALERT - IF I CONVERT TO INTEGER IT WILL REMOVE THE FIRST 0 - BINARY WILL NOT WORK
        print (bin4trChar)
    #need to convert to bytes type object 
    #bin4trChar = int(bin4trChar)
    #bin4trChar = (bin4trChar).to.
    #aChar = binascii.b2a_uu(bin4trChar)
    #aChar = str(aChar)
    #TRS = TRS + aChar


print (Encodee)
print (TRS)


