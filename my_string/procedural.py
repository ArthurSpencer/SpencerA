binaryholder = []
final = ""
string = "BdjaHBBDa"
print(string)
binaryholder = list(string)
letter = ""
for counter in range (0, len(string)):
    letter = binaryholder[counter]
    letter = ord(letter)
    if letter > 96:
        letter = letter - 32
        letter = chr(letter)
        binaryholder[counter] = letter
    #endif
#next
print (binaryholder)
