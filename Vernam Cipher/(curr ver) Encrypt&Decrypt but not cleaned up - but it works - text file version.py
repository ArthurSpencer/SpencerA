#Other Stuff: Have it export to text file and also have it truly random 
#Good chance it wont work with others' - others may have used a whole byte - whole extended ascii/unicode

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
        while denary != 0:
            remainder = denary % 2
            denary = denary // 2
            fbtemppt = str(remainder) + fbtemppt
        #endwhile
        while len(fbtemppt) < 7:
            fbtemppt = "0" + fbtemppt
        #endwhile
        binaryPTa.append(fbtemppt)


        fbtemptrs = ""
        denary = (TRSproto[counter])
        while denary != 0:
            remainder = denary % 2
            denary = denary // 2
            fbtemptrs = str(remainder) + fbtemptrs
        #endwhile
        while len(fbtemptrs) < 7:
            fbtemptrs = "0" + fbtemptrs
        #endwhile
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
        
        encryptedXOR = ''

       
    print ("Proof of XOR:")
    print ("Key Binary:")
    print (binaryTRSa)
    print ("Plain Text Binary:")
    print (binaryPTa)
    print ("Encrypted Text Binary:")
    print (encryptedBinary)

    encryptedLetters = ""
    for counter in range (lengthEncodee):
        temp = int(encryptedBinary[counter], 2)
        temp = chr(temp)
        encryptedLetters = encryptedLetters + temp


    print ("Encrypted Message: " + encryptedLetters)

    f= open(encodee + " Key","w+")
    f.write(TRS)
    f= open(encodee + " Encrypted Message","w+")
    f.write(encryptedLetters)


def SalieriDec(text,key):
    lengthEncodee = len(text)
    TRS = ''
    binaryPT = ''
    binaryTRS = ''
    binaryPTa = []
    binaryTRSa = []
    print ("Your encoded text is: " + (text))
        
    print ("Your decryption key is: " +(key))

    ### - conversion to arrays of letters 

    PTproto = list(text)
    TRSproto = list(key)
    encryptedBinary = []

    ### - conversion to arrays of binary digits
    
    for counter in range (lengthEncodee):
        # - turns into denary of ascii
        PTproto[counter] = ord(PTproto[counter])
        TRSproto[counter] = ord(TRSproto[counter])
        
        
        fbtemppt = ""
        denary = (PTproto[counter])
        while denary != 0:
            remainder = denary % 2
            denary = denary // 2
            fbtemppt = str(remainder) + fbtemppt
        #endwhile
        while len(fbtemppt) < 7:
            fbtemppt = "0" + fbtemppt
        #endwhile
        binaryPTa.append(fbtemppt)


        fbtemptrs = ""
        denary = (TRSproto[counter])
        while denary != 0:
            remainder = denary % 2
            denary = denary // 2
            fbtemptrs = str(remainder) + fbtemptrs
        #endwhile
        while len(fbtemptrs) < 7:
            fbtemptrs = "0" + fbtemptrs
        #endwhile
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
        
        encryptedXOR = ''

       
    print ("proof of XOR:")
    print ("Key Binary:")
    print (binaryTRSa)
    print ("Encrypted Message Binary:")
    print (binaryPTa)
    print ("Plain Text Binary:")
    print (encryptedBinary)

    encryptedLetters = ""
    for counter in range (lengthEncodee):
        temp = int(encryptedBinary[counter], 2)
        temp = chr(temp)
        encryptedLetters = encryptedLetters + temp


    print ("Decrypted Message: " + encryptedLetters)

    f= open(" Decrypted Message","w+")
    f.write(encryptedLetters)
  
#EndProcedure

end = False 
while end == False:
    inp = False 
    first = input('Encrypt ("e") or Decrypt ("d")?\n')
    if first == ("e") or first == ("d"):
        inp = True
    else:
        inp = False 
    #endif
    while inp == False:
        first = input('Encrypt ("e") or Decrypt ("d")?\n')
        if first == "e" or first == "d":
            inp = True

    if first == "e":
        encodee = input("Message To Encode:\n")
        SalieriEnc(encodee)

    elif first == "d":
        
        text = input("Enter Encrypted Text:\n")
        key = input("Enter the key:\n")
        SalieriDec(text,key)

    inp = False
    tempend = input('Finished? - Yes ("y") or No ("n")\n')
    if tempend == ("y"):
        inp = True
        end = True
    elif tempend == ("n"):
        inp = True
        end = False
    else:
        inp = False
    while inp == False:
        tempend = input('Finished? - Yes ("y") or No ("n")\n')
        if tempend == "y" or tempend == "n":
            inp = True

    if tempend == ("y"):
        inp = True
        end = True
    elif tempend == ("n"):
        inp = True
        end = False
    
    

