# Download DB Browser for SQLite so you can see the table like microsoft access

import sqlite3
import datetime
import time
from ProfileClothing import profile
from ProfileClothing import clothing
import os

#For clearing cmd
clear = lambda: os.system('cls')


#Connect to the database
conn = sqlite3.connect('clothinator.db')
#Some sort of abstract thing that acts as the link between database and program
c = conn.cursor()

#Checks in the Profile table to see if there is an account/accounts already made
def checkaccount():
    #print("Checking if an account exists")
    c.execute("Select username FROM profiles")
    check = (str(c.fetchone()))
    return check

#Allows the user to choose which Profile they would like to use (Which has their email/time of email and connects to their clothing library
def chooseaccount():
    clear()
    c.execute("Select username FROM profiles")
    print(c.fetchall())
    print("Choose your account")


    #variables need to be passed to the class/object
    pass

#Allows the user to make an account (details go into database)
def makeaccount():
    clear()
    print("Time to make your Account!")
    username = input("What would you like your username to be?\n")
    c.execute("Select * FROM profiles WHERE username =:username", {'username': username})
    #print(str(c.fetchone()))
    check = (str(c.fetchone()))
    #print (x)
    #If nothing is found then None would be returned - If None is not returned then a username with that name must already exist
    
    while check != "None":
        username = input("That username is already in use, please choose another\n")
        c.execute("Select * FROM profiles WHERE username =:username", {'username': username})
        check = (str(c.fetchone()))
    #endwhile

    email = input("What is your email?\n")
    emailtime = input("What time would you like your email?\n")
    acc_1 = profile(username,email,emailtime)
    #print(acc_1.getUsername())

    #Inserts values into the profile table in the database
    c.execute("INSERT INTO profiles VALUES (:username, :email, :emailtime)", {'username': acc_1.username, 'email': acc_1.email, 'emailtime': acc_1.emailtime})
    conn.commit()

    clear()

    print("Your Account has been created... Time to add clothing! - Enter '/' once you have finished")

    #clothingname = "doesntmatter"
    #while clothingname != "/":
    #    username = acc_1.username
    #    clothingname = input("Name:\n")
    #    bodycat = input("What category of clothing does this go into?: Hat, Scarf, Gloves, Jacket, Jumper, Shirt, Bottoms, Socks\n").lower()
    #    while bodycat != ["hat", "scarf", "gloves", "jacket", "jumper", "shirt", "bottoms", "socks"]:
    #        bodycat = input("What category of clothing does this go into?: Hat, Scarf, Gloves, Jacket, Jumper, Shirt, Bottoms, Socks\n").lower()
    #    #endwhile
    ##endwhile

    #For keeping track of what has been entered
    clothinglist = []

    brk = False
    while brk != True:
        username = acc_1.username
        clothingname = input("Name of item:\n")
        if clothingname ==  ("/"):
            brk = True
            break 
        bodycat = input("What category of clothing does this go into?: Hat, Scarf, Gloves, Jacket, Jumper, Shirt, Bottoms, Socks\n").lower()
        while bodycat not in ["hat", "scarf", "gloves", "jacket", "jumper", "shirt", "bottoms", "socks"]:
            bodycat = input("What category of clothing does this go into?: Hat, Scarf, Gloves, Jacket, Jumper, Shirt, Bottoms, Socks\n").lower()
        warmth = int(input("On a scale of 0 to 100 (100 being warmest) How warm is this piece of clothing?\n"))
        while warmth not in range (0,100):
            warmth = int(input("On a scale of 0 to 100 (100 being warmest) How warm is this piece of clothing?\n"))


        clo_1 = clothing(username,clothingname,bodycat, warmth)
        c.execute("INSERT INTO clothing VALUES (:username, :clothingname, :bodycat, :warmth)", {'username': clo_1.username, 'clothingname': clo_1.clothingname, 'bodycat': clo_1.bodycat, 'warmth': clo_1.warmth})
        conn.commit()

        clothinglist.append(clo_1.clothingname)

        clear()
        #Add a list that is printed on refresh to show which items have been entered 
        print("You have entered ", clothinglist)
        print("Enter '/' once you have finished")

    



#Making the tables """ """ allows for comments over multiple lines

def tablemaker():
    c.execute("""
    CREATE TABLE profiles
    (
    username text,
    email text,
    emailtime integer
    )
    """)

    conn.commit()

    c.execute("""
    CREATE TABLE clothing
    (
    username text,
    clothingname text,
    clothingcategory text,
    Warmth integer,
    FOREIGN KEY (username) REFERENCES profiles(username)
    )
    """)

    conn.commit()


#Start of the program - Options to either choose a profile or make a new one 
def starter():
    yn = input("Do you already have a profile?\n").lower()

    while yn not in ["yes","no"]:
        yn = input("Do you already have a profile? - enter Yes or No\n").lower()
      
    return yn
    #endwhile
   
#For making tables
#tablemaker()



yn = starter()
check = checkaccount()
if (yn == "yes") and (check != "None"):
    chooseaccount()
elif (yn == "yes") and (check == "None"):
    print("You need to make an account, none are stored")
    makeaccount()
    chooseaccount()
else:     
    makeaccount()
    chooseaccount()
#endif
