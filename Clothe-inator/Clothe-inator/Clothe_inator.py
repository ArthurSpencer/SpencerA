import sqlite3
import datetime
import time
import os
import ssl
from email.mime.text import MIMEText
from ProfileClass import profile
from ClothingClass import clothing

#for clearing cmd
clear = lambda: os.system('cls')

#Connect to the database
conn = sqlite3.connect('databaseofneededstuff.db')
#Some sort of abstract thing that acts as the link between database and program
c = conn.cursor()


### NOTES
### remember I have to pass the classes arround to functions (actually might be the reason its good to use classes 
#- all the values are packaged up and easy to move to different functions instead of passing each variable seperately

# - Make a function for choosing the clothingtype(finding it to select it)
#Watch out about referential integrity

# - remember to comitt after every change to the database
###

#Make Verification check function
#While Match Not True
#attribute will be email or username - so it displays the right message 
#If not true then keep doing verification
def Verification(attribute):
    check1 = input("Enter in your", attribute,)
    check2 = input("Re-Enter your", attribute,)
    if check1 == check2:
        return True
    else: 
        "These do not match"
        return False

def tablemaker():

    c.execute("""
    CREATE TABLE profiletable
    (
    username text,
    email text,
    emailtime text,
    algorithmtype text
    )
    """)

    conn.commit()

    c.execute("""
    CREATE TABLE itemtable
    (
    username text,
    clothingname text,
    clothingtypekey text,
    temprangemin integer,
    temprangemax integer,
    FOREIGN KEY (clothingtypekey) REFERENCES  clothinginfotable(clothingtypekey)
    FOREIGN KEY (username) REFERENCES profiletable(username)
    )
    """)

    conn.commit()

    c.execute("""
    CREATE TABLE clothinginfotable
    (
    clothingtypecategory text,
    clothingtypekey text,
    clovalue integer

    )
    """)

    conn.commit()

    c.execute("""
    CREATE TABLE triptable
    (
    tripid text,
    username text,
    date text,
    time text,
    temp integer,
    windspeed integer,
    adjustedtemp integer,
    activitylevel text,
    calculatedclo integer,
    underwearpants text,
    underwearshirts text,
    shirts text,
    trousers text,
    coveralls text,
    highlyinsulatingcoveralls text,
    sweaters text,
    jacket text,
    coatsandoverjacketsandovertrousers text,
    socks text,
    shoes text,
    skirtsdresses text,
    sleepwear text,
    robes text,

    FOREIGN KEY (username) REFERENCES profiletable(username)
    )
    """)

    conn.commit()

### deleting a username means deleting every instance of that username from trip table and item item table
### But if clothing deleted - u dont want it deleted from the trip table - doesnt matter cos in that instance wont exist
### you arent going to be running algorithm on previous days when the data no longer exists

### Just copy the ClothingInfoTable in with db broswer - its not worth it 

#To make tables if they don't exist in the database (database is auto initialised)
#Remember to make Username, Clothingname, Clothingtypekey and TripID primary keys
#Never delete the ClothingInfoTable - it should just be a static table that is never changed - just used to retrieve data and inform

###tablemaker()
#comment out tablemaker after first run



def start():
    yn = input("Do you already have a profile?\n").lower()
    while yn not in ["yes","no"]:
        yn = input("Do you already have a profile? - enter Yes or No\n").lower()
    check = checkaccount()
    if (yn == "yes") and (check != "None"):
        acc_1 = chooseaccount()
    elif (yn == "yes") and (check == "None"):
        print("You need to make an account, none are stored")
        makeaccount()
        chooseaccount()
    else:
        makeaccount()
        chooseaccount()
    pass
#Gives option to either makeaccount() or allows the user to chooseaccount() as long as checkaccount() does not pass None (as long as accounts exist)

def checkaccount():
    c.execute("Select username FROM profile")
    check = (str(c.fetchone()))
    return check
    
    pass
#(edit it so the check actually happens in the function and returns present or not present to make it more understandable)
#Used when choosing an account to make sure they exist 

def makeaccount():
    clear()
    print("Time to make your Account!")
    username = input("What would you like your username to be?\n")
    c.execute("Select * FROM profiletable WHERE username =:username", {'username': username})
    #print(str(c.fetchone()))
    check = (str(c.fetchone()))
    #print (x)
    #If nothing is found then None would be returned - If None is not returned then a username with that name must already exist
    
    while check != "None":
        username = input("That username is already in use, please choose another\n")
        c.execute("Select * FROM profiletable WHERE username =:username", {'username': username})
        check = (str(c.fetchone()))
    #endwhile

    email = input("What is your email?\n")
    emailtime = input("What time would you like your email?\n")
    acc_1 = profile(username,email,emailtime)
    #print(acc_1.getUsername())

    #Inserts values into the profile table in the database
    c.execute("INSERT INTO profiletable VALUES (:username, :email, :emailtime)", {'username': acc_1.username, 'email': acc_1.email, 'emailtime': acc_1.emailtime})
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
        c.execute("INSERT INTO itemtable VALUES (:username, :clothingname, :bodycat, :warmth)", {'username': clo_1.username, 'clothingname': clo_1.clothingname, 'bodycat': clo_1.bodycat, 'warmth': clo_1.warmth})
        conn.commit()

        clothinglist.append(clo_1.clothingname)

        clear()
        #Add a list that is printed on refresh to show which items have been entered 
        print("You have entered ", clothinglist)
        print("Enter '/' once you have finished")
    pass
#When user inputs username, first check userbanes 
#Make a new account - choose profile details and populate clothing library

def chooseaccount():
    clear()
    c.execute("Select username FROM profiletable")
    accountlist = (c.fetchall())
    c.execute("Select username FROM profiletable")
    display = (c.fetchall())


    #### Scary Loop
    
    leng = len(accountlist)

    for counter in range(leng):
        changevariable = str(accountlist[counter]).lower()
        accountlist[counter] = changevariable
    
    #print(accountlist) # otherwise lowercase
    print(display)

    #### End of Scary Loop
    ####
    #print(accountlist)

    accountinput = input("Choose your account\n")

    profinput = ("('" + accountinput + "',)").lower()
    #print(profinput)

    clear()

    #print(accountlist)
    #print(str(accountlist[1]))
    #print(accountinput)
    #print(profinput)


    ####
    #If I convert it to a str then whole list format becomes string as is really janky - dont use
    #
    #Need to convert the list to a better form - so don't get an error from it not being an actual username but letters in the username
    #Then add it into the loop below - also lower case --- Sp should not pass SpencerA
    while profinput not in (accountlist):
        #clear()
        print(display)
        accountinput = input("Choose an account from the list\n")
        profinput = ("('" + accountinput + "',)").lower()


    #c.execute("SELECT * FROM profiles WHERE username=:accountinput", {'accountinput': accountinput})
    c.execute("SELECT * FROM profiles WHERE username LIKE :accountinput", {'accountinput': accountinput}) #lowercase stuff
    accountfetch = c.fetchall()

    clear()

    print("Logging In")
    #print(accountfetch)
    #print(accountfetch[0])
    username = accountfetch[0][0] ###ITS A DAMN NESTED LIST YA FOOL
    email = accountfetch[0][1]
    emailtime = accountfetch[0][2]
    acc_1 = profile(username,email,emailtime)

    #
    print("Your username is:", acc_1.getUsername())
    print("Your email is:", acc_1.getEmail())
    print("You will be sent an email at:",acc_1.getEmailtime())
    print("")

    #

    #variables need to be passed to the class/object

    return acc_1
    pass
#Choose account from list

def profilemenu():
    pass
#Gives options that even pass onto reccomendnow, profile details, clothing details, back to start choices or activates the reccomendation at a given time

def profiledetails():
    pass
#Shows profile details
#Allows user to change username, email, emailtime, algtype or to delete the account
#if account deleted - everything in database with that username must be deleted 
#User then would be passed back to start

def clothingdetailsoptions():
    pass
#Lists clothing and then: lets user pick a piece of clothing from that list - 

def clothingdetails():
    pass
#Shows stuff about that particular piece of clothing
#User can then change the name or type of the clothing - depending on which decision is chosen, passes to different proc in class
#Or user has choice to delete the piece of clothing - again in class

def clothingtypechooser():
    pass
#basically spits out clothing info table and lets user go through it to choose the type
#shows all clothingtypecategories and lets user choose which
#then shows all clothingtypekey and lets user choose which
#then assigns that clothingname record in the table with that clothingtypekey so clo value can be retrieved later
#allows user to move between layers of the table

def reccomend():
    pass
#Contains the calls to functions to reccomend an outfit

def weatherget():
    pass
#gets values for windspeed and temperature
#if windspeed > certain amount then find windchill to get adjusted temp
#else adjustedtemp = temperature 

def windchillcalc():
    pass
#gets adjusted temperature accounting for windchill

def clocalc():
    pass
#calculates the clovalue that would be needed for the adjusted temperature

def permutationrunner():
    pass
#runs through every single possible combination of clothing
#creates list with all of the clothing possibilities and the clo value
#Also to make it run possibilities without each option

def permutationchooser():
    pass
#chooses best permutation from a list of the possible combinations
#first finds second quartile around the clo value target
#then runs logic to find which combinations are stupid - e.g. shoes but no socks, or not having shoes
#Maybe I could make an sql table that holds all of these possibilites, then i could do something like, delete from permutationchoosetable where socks = null 
#that would help cut down a lot
#Then at the end, once the code has chosen a combination and put it into the triptable, delete all values in the permutation chooser table

def email():
    pass
#sends the email with the clothes from the permutation chooser to the email stored for the profile

def userfeedbackupdate():
    pass

### Main Program
#tablemaker()
###^dup do not uncomment


print("Table made")
start()

("You got out")
###
### Main calling program - hopefully should never be broken out of, because all functions refer to different functions - they dont refer to self so hopefully no stack overflow recursion errors 
