import os
import random

print ("Would you like to play?")
print ("Credit: 100")
print ("Each spin costs 20 credits")
wait = input("Press Enter to Continue")

poss = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
ch = []
Credit = 100
goagain = True
while goagain == True:
    Credit = Credit - 20
    ch = []
    for i in range(3):
        ch.append(random.choice(poss))
    for i in range(3):
        print(ch[i])
    if ch[0] == "Skull" and ch[1] == "Skull" and ch[2] == "Skull":
        Credit = 0
    elif (ch[0] == "Skull" and ch[2] == "Skull") or (ch[1] == "Skull" and ch[2] == "Skull") or (ch[0] == "Skull" and ch[2] == "Skull"):      
        Credit = Credit - 100 
    elif ch[0] == "Bell" and ch[1] == "Bell" and ch[2] == "Bell":
        Credit = Credit + 500
    elif (ch[0] == ch[1]) and (ch[0] == ch[2]):
        Credit == Credit + 100
    elif ((ch[0] == ch[1]) or (ch[1] == ch[2]) or (ch[0] == ch[2])):
        Credit = Credit + 50
    else:
        Credit = Credit
    #endif

    print(Credit)

    print("Again? y/n")
    inp = input()
    if inp == "y":
            goagain = True
    else:
            goagain = False
    #endif
      
    if(goagain) == False or (Credit < 20):

        exit()

    os.system('cls')
    #endif
#endwhile

