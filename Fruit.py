import os
import random

print ("Would you like to play?")
print ("Credit: 100")
print ("Each spin costs 20 credits")
wait = input("Press Enter to Continue")

#problems
#if a single Skull is R2 or R3 then -100
#if r1 and r2 are the same it doesnt work but if r1 == r3 or r2 == r3 it does
#Need to fix it so it recognises skulls as a collective and also recognises the first position

poss = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
Credit = 100
goagain = True
while goagain == True:
    Credit = Credit - 20
    R1 = (random.choice(poss))
    R2 = (random.choice(poss))
    R3 = (random.choice(poss))
    print (R1,R2,R3)
    if (R1 == "Skull" and  R2 == "Skull" and R3 == "Skull"):
        Credit = 0
    elif ((R1 and R2 == "Skull") or (R2 and R3 == "Skull") or (R1 and R3 == "Skull")):  
        Credit = Credit - 100
    elif (R1 == "Bell" and R2 == "Bell"  and R3 == "Bell"):
        Credit = Credit + 500
    elif (R1 == R2 == R2):
        Credit == Credit + 100
    elif ((R1 == R2) or (R2 == R3) or (R1 == R3)):
        Credit = Credit + 50
    else:
        Credit = Credit

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
    #endif

    os.system('cls')
#endwhile
