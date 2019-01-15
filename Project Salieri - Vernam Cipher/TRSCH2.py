#Other Stuff: Have it export to text file and also have it truly random 
#Good chance it wont work with others' - others may have used a whole byte - whole extended ascii/unicode
# - bin(dec)

import random
import binascii 

def SalieriEnc(encodee):
    lengthEncodee = len(encodee)
    TRS = ''
    binaryPT = ''
    binaryTRS = ''
    binaryPTa = []
    binaryTRSa = []
    print ("Your plain text is: " + (encodee))
    for counter in range (0, len(encodee)):
        rand = random.getrandbits(7)
        #print(rand)
        rand = chr(rand)
        TRS = TRS + rand
    #next
        
    print ("Your encryption key is: " +(TRS) + " and has been exported to a text file")

    ### - conversion to arrays of letters 

    PTproto = list(encodee)
    TRSproto = list(TRS)
    encryptedBinary = []

    ### - conversion to arrays of binary digits
    
    for counter in range (lengthEncodee):
        # - turns into denary of ascii
        PTproto[counter] = ord(PTproto[counter])
        TRSproto[counter] = ord(TRSproto[counter])
        
        
        fbtemppt = ""
        denary = (PTproto[counter])
        #denary = int(denary)
        while denary != 0:
            remainder = denary % 2
            denary = denary // 2
            fbtemppt = str(remainder) + fbtemppt
        #endwhile
        while len(fbtemppt) < 7:
            fbtemppt = "0" + fbtemppt
        #endwhile
        #print(fbtemppt)
        binaryPTa.append(fbtemppt)


        fbtemptrs = ""
        denary = (TRSproto[counter])
        #denary = int(denary)
        while denary != 0:
            remainder = denary % 2
            denary = denary // 2
            fbtemptrs = str(remainder) + fbtemptrs
        #endwhile
        while len(fbtemptrs) < 7:
            fbtemptrs = "0" + fbtemptrs
        #endwhile
        #print(fbtemptrs)
        binaryTRSa.append(fbtemptrs)



    encryptedXOR = ''
    for byte in range (lengthEncodee):
        for bit in range (7):
            checkPlainText = (binaryPTa[byte][bit])
            checkRandomKey = (binaryTRSa[byte][bit])
            if checkPlainText != checkRandomKey:
                encryptedXOR = encryptedXOR + '1'
            else:
                encryptedXOR = encryptedXOR + '0'
                

        encryptedBinary.append(encryptedXOR)
        #print (encryptedBinary)
        encryptedXOR = ''

        #while len(encryptedtemp) < 7:
            #encryptedtemp = "0" + encryptedtemp
        #endwhile
        
    #print (rand)
    print ("proof of XOR")
    print (binaryTRSa)
    print (binaryPTa)
    print (encryptedBinary)

    encryptedLetters = ""
    for counter in range (lengthEncodee):
        temp = int(encryptedBinary[counter], 2)
        temp = chr(temp)
        encryptedLetters = encryptedLetters + temp


    print ("Encrypted Message: " + encryptedLetters)

    #print(encryptedBinary[0])
    #temp = int(encryptedBinary[0], 2)
    #print (temp)
    #next

    #print (encryptedLetters)
    #print (TRS)


##    encryptedLetters = ""
##    for counter in range (lengthEncodee):
##        encryptedBinary[counter] = int(encryptedBinary[counter])
##        encryptedBinary[counter] = chr(encryptedBinary[counter])
##        print (encryptedBinary[counter])
##        
##        encrypedLetters = encryptedLetters + encryptedBinary[counter]
##    #next
##
##    print (encryptedLetters)
##    print (TRS)

    


        
            
            
        
        
    
    

inp = False 
first = input('Would you like to encrypt ("e") or decrypt ("d")?\n')
if first == ("e") or first == ("d"):
    inp = True
else:
    inp = False 
#endif
while inp == False:
    first = input('Please enter "e" or "d"\n')
    if first == "e" or first == "d":
        inp = True

if first == "e":
    encodee = input("What message would you like to encode\n")
    SalieriEnc(encodee)


