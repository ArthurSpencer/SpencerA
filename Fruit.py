import random
poss = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
Credit = 100
goagain = True
while True:
    Credit = Credit - 20
    R1 = (random.choice(poss))
    R2 = (random.choice(poss))
    R3 = (random.choice(poss))
    Print (r1,r2,r3)
    if R1 and R2 and R3 == "Skull":
        Credit = 0
    elif (R1 and R2) or (R2 and R3) or (R1 and R3) == "skull":  
        Credit == Credit - 100
    elif R1 and R2 and R3 == "Bell":
        Credit == Credit + 500
    elif R1 == R2 == R2:
        Credit == Credit + 100
    elif (R1 == R2) or (R2 == R3) or (R1 == R3):
        Credit == Credit + 50
   
    print(Credit)

    print("Again?, "" or n "")
      
        if inp = "y":
            goagain = True else goagain = False
      
if condition: ((goagain) == False) or (Credit < 20) break

