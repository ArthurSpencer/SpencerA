import sqlite3
import datetime
import sched
import time
import os
import ssl
from email.mime.text import MIMEText
from ProfileClass import profile
from ClothingClass import clothing
import datetime
import _thread
import timeit
import threading
from multiprocessing import Process
import sys
import pyowm
import statistics


owm = pyowm.OWM('19869702ff812dc8fab95ff8ddffec2f')






#from datetime import datetime


#for clearing cmd
clear = lambda: os.system('cls')

#Connect to the database
conn = sqlite3.connect('databaseofneededstuff.db', check_same_thread=False)
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
def verification(attribute):
    
    match = False
    while match == False:
        check1 = input("Enter in your " + attribute + "\n")
        check2 = input("Re-Enter your " + attribute + "\n")
        if check1 == check2:
            clear()
            return check1
            match = True
            
        else: 
            clear()
            print("These do not match")
            match = False

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
    temprangemax integer

    )
    """)

    conn.commit()

    #c.execute("""
    #CREATE TABLE clothinginfotable
    #(
    #clothingtypecategory text,
    #clothingtypekey text,
    #clovalue integer

    #)
    #""")

    #conn.commit()

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
    robes text

    
    )
    """)

    conn.commit()


#For itemtable
#FOREIGN KEY (clothingtypekey) REFERENCES  clothinginfotable(clothingtypekey)
#FOREIGN KEY (username) REFERENCES profiletable(username)

#For trip table
#FOREIGN KEY (username) REFERENCES profiletable(username)

### deleting a username means deleting every instance of that username from trip table and item item table
### But if clothing deleted - u dont want it deleted from the trip table - doesnt matter cos in that instance wont exist
### you arent going to be running algorithm on previous days when the data no longer exists

### Just copy the ClothingInfoTable in with db broswer - its not worth it 

#To make tables if they don't exist in the database (database is auto initialised)
#Remember to make Username, Clothingname, Clothingtypekey and TripID primary keys
#Never delete the ClothingInfoTable - it should just be a static table that is never changed - just used to retrieve data and inform
 


def starter():
    exit = False
    while exit == False:
        possible = [1,2]

        print("""
    Clothe-inator

        ( 1 ) Choose Account
        ( 2 ) Make Account
        """)
        selection = input("    What would you like to do?\n")
        check = checkaccount()
        if (selection == "1") and (check != "None"):
            clear()
            chooseaccount()
        elif (selection == "1") and (check == "None"):
            clear()
            print("You need to make an account, none are stored")
            makeaccount()
            chooseaccount()
        elif (selection == "2"):
            clear()
            makeaccount()
            chooseaccount()
        else:
            print("This number option cannot be selected")

        #yn = input("Do you already have a profile?\n").lower()
        #while yn not in ["yes","no"]:
        #    yn = input("Do you already have a profile? - enter Yes or No\n").lower()
        #check = checkaccount()
        #if (yn == "yes") and (check != "None"):
        #    clear()
        #    chooseaccount()
        #elif (yn == "yes") and (check == "None"):
        #    clear()
        #    print("You need to make an account, none are stored")
        #    makeaccount()
        #    chooseaccount()
        #else:
        #    clear()
        #    makeaccount()
        #    chooseaccount()
        #pass
#Gives option to either makeaccount() or allows the user to chooseaccount() as long as checkaccount() does not pass None (as long as accounts exist)

def checkaccount():
    c.execute("Select username FROM profiletable")
    check = (str(c.fetchone()))
    return check
    
    pass
#(edit it so the check actually happens in the function and returns present or not present to make it more understandable)
#Used when choosing an account to make sure they exist 

def makeaccount():
   print("Time to make your Account!")
   attribute = "username"
   username = input("Enter Username\n")
   c.execute("Select * FROM profiletable WHERE username =:username", {'username': username})
   checkusername = (str(c.fetchone()))
   #If check does not equal to none then that username must already exist in some form
   while checkusername != "None":
       username = input("That username is already in use, please choose another\n")
       username = input("Enter Username\n")
       c.execute("Select * FROM profiletable WHERE username =:username", {'username': username})
       checkusername = (str(c.fetchone()))
    #endwhile
   attribute = "email"
   email = verification(attribute)
   clear()

   timeformat = "%H:%M"
   inputtime = False
   while inputtime == False:
       emailtime = input("What time would you like your email? (hh:mm) \n")
       try: 
           validtime = datetime.datetime.strptime(emailtime, timeformat)
           inputtime = True
       except ValueError:
           clear()
           print("Not in the correct format, please try again")

    
   algtype = "clo"
   acc_1 = profile(username,email,emailtime,algtype)
   c.execute("INSERT INTO profiletable VALUES (:username, :email, :emailtime, :algtype)", {'username': acc_1.username, 'email': acc_1.email, 'emailtime': acc_1.emailtime, 'algtype': acc_1.algtype})
   conn.commit()
   clear()

   ###
   #x = input("stop")
   ###


   #ClothingEntersql
   #Take the object returned from the function and then put it into the table as a new entry
   clothinglist = []

   
   print("Time to make your clothing library")

   end = False
   while end == False:
        makeacc = True
        cl_1 = enterclothing(acc_1.username, makeacc)
        c.execute("INSERT INTO itemtable VALUES (:username, :clothingname, :clothingtypekey, :temprangemin, :temprangemax)", {'username': cl_1.username, 'clothingname': cl_1.clothingname, 'clothingtypekey': cl_1.clothingtypekey, 'temprangemin': cl_1.temprangemin, 'temprangemax': cl_1.temprangemax})
        conn.commit()
        clear()
        clothinglist.append(cl_1.clothingname)
        inploop = True
        while inploop == True:
            print("You have entered ", clothinglist)
            ans = input("Another? (y/n)").lower()
            if ans == "y":
                end = False
                inploop = False
            elif ans == "n":
                end = True
                inploop = False
            else:
                clear()





   pass
#When user inputs username, first check usernames 
#Make a new account - choose profile details and populate clothing library

def enterclothing(username, makeacc):
    username = username
    clothingname = input("What is the name of your item\n")
    clothingtypekey = clothingtypechoosermenu(makeacc)


    c.execute("SELECT max, min FROM clothinginfotable WHERE clothingtypekey LIKE :clothingtypekey", {'clothingtypekey': clothingtypekey}) #lowercase stuff
    temps = c.fetchall()
    print(temps)
    temprangemax = temps[0][0]
    temprangemin = temps[0][1]
    cl_1 = clothing(username,clothingname, clothingtypekey, temprangemin, temprangemax)
    return cl_1
    #User chooses clothing name

    #then go to clothingtypechooser and return clothingtypekey
    pass

def chooseaccount():
    clear()

    c.execute("Select username FROM profiletable")
    queryoutput = (c.fetchall())
    lenofqueryoutput = len(queryoutput)

    #print(queryoutput)
    #print(lenofqueryoutput)
    #stop = input("stop")

    accountlist = []
    for counter in range(lenofqueryoutput):
        toadd = queryoutput[counter][0]
        if toadd not in accountlist:
            accountlist.append(toadd)
        pass
    print("Which account would you like to use?")
    exit = False
    while exit == False:
        lenofaccountlist = len(accountlist)
        optionlist = []
        for counter in range(lenofaccountlist):
            optionlist.append(str(counter + 1))
            print("(", counter + 1, ")", accountlist[counter] )    
        print("( / )", "Start Menu")
    
        selection = input("Choose your account\n")
        if selection == "/":
            clear()
            starter()
        elif selection not in optionlist:
            clear()
            print("This number option cannot be selected")
        else:
            selection = int(selection) - 1
            accountinput = (accountlist[selection])
            #stop = input("stop")

            c.execute("SELECT * FROM profiletable WHERE username LIKE :accountinput", {'accountinput': accountinput}) #lowercase stuff
            accountfetch = c.fetchall()
    

            username = accountfetch[0][0] 
            email = accountfetch[0][1]
            emailtime = accountfetch[0][2]
            algtype = accountfetch[0][3]
            acc_1 = profile(username,email,emailtime,algtype)

            profilemenu(acc_1)


        


     






    ########################################################################################################################################### -- Disgusting Code

    #c.execute("Select username FROM profiletable")
    #accountlist = (c.fetchall())
    #c.execute("Select username FROM profiletable")
    #display = (c.fetchall())




    ##### Scary Loop
    
    #leng = len(accountlist)

    #for counter in range(leng):
    #    changevariable = str(accountlist[counter]).lower()
    #    accountlist[counter] = changevariable
    
    ##print(accountlist) # otherwise lowercase
    #print(display)
    #print("( / ) to exit to starter")
    ##### End of Scary Loop
    #####
    ##print(accountlist)

    #accountinput = input("Choose your account\n")

    #if accountinput == "/":
    #    clear()
    #    starter()


    #profinput = ("('" + accountinput + "',)").lower()
    ##print(profinput)

    #clear()

    ##print(accountlist)
    ##print(str(accountlist[1]))
    ##print(accountinput)
    ##print(profinput)


    #####
    ##If I convert it to a str then whole list format becomes string as is really janky - dont use
    ##
    ##Need to convert the list to a better form - so don't get an error from it not being an actual username but letters in the username
    ##Then add it into the loop below - also lower case --- Sp should not pass SpencerA
    #while profinput not in (accountlist):
    #    #clear()
    #    print(display)
    #    accountinput = input("Choose an account from the list\n")
    #    profinput = ("('" + accountinput + "',)").lower()

    #clear()
    #print("")

    ########################################################################################################################################### -- Disgusting Code



    #c.execute("SELECT * FROM profiletable WHERE username LIKE :accountinput", {'accountinput': accountinput}) #lowercase stuff
    #accountfetch = c.fetchall()
    

    #username = accountfetch[0][0] 
    #email = accountfetch[0][1]
    #emailtime = accountfetch[0][2]
    #algtype = accountfetch[0][3]
    #acc_1 = profile(username,email,emailtime,algtype)

    #profilemenu(acc_1)


#Choose account from list

def timer(acc_1, seconds):
    while seconds > 0:
        seconds = seconds - 1
        time.sleep(1)
        if seconds == 0:
            t = True
            #reccomend(acc_1)

    
    pass

def prerec(acc_1):
    reccomend(acc_1)
    
    pass

def profilemenu(acc_1):

    ###t.cancel - to override


    #stop = input("stop1")
    emailtime = acc_1.getEmailTime()


    
    


    #find difference between timenow and rectime
    #set a time for difference
    #if rec now is activated then cancel timer
    #if timer gets to 0 - activate rec function
    
    #alarmtime = '06:00'
    #print(currenttime)


    currenttime = (datetime.datetime.now().strftime('%H:%M'))
    
    FMT = '%H:%M'
    timertime = datetime.datetime.strptime(emailtime, FMT) - datetime.datetime.strptime(currenttime, FMT)

    #stop = input("stop2")

    ###

    if timertime < datetime.timedelta(days=0):
        timertime = ((timertime) + datetime.timedelta(days=1))
        pass
    

    #t = timeit.Timer(timertime,reccomend)
    
    #st = input("stop")

    timertime = str(timertime)
    #print(timertime)
    h, m, s = timertime.split(':')
    
    ####
    seconds = (int(h) * 3600) + (int(m) * 60) + (int(s))
    #t = threading.Thread(target=timer, args=(acc_1,3))
    #t.start()


    #pt = Process(target = timer, args=(acc_1, seconds))
    #pt.start()

    #global t
    #t = threading.Timer(5, prerec, [acc_1])
    #t.start()


    
    #stop = input("st")
    #stop = input("st")

    #timer (acc_1, seconds)

    ####

    #print(seconds)
    #stop = input("stop3")

    #print(h)
    #print(m)
    #print(s)
    
    #stop = input("stop")

    #print(timertime)
    #print(seconds)
    #st = input("stop")
    #global t
    #t = threading.Timer(seconds, reccomend, [acc_1])
    
    #t.starter()
    clear()

    #stop = input("stop4")

    ####
    #print(timertime)
    ####


    #s = sched.scheduler(time.time, time.sleep)
    #print(seconds)
    #s.enter(1, 1, reccomend, argument=(acc_1,))
    #s.run()

    #stop = input("stop")

    ans = False
    while ans == False:

        c.execute("SELECT * FROM profiletable WHERE username LIKE :accountinput", {'accountinput': acc_1.username}) #lowercase stuff
        accountfetch = c.fetchall()
    

        username = accountfetch[0][0] 
        email = accountfetch[0][1]
        emailtime = accountfetch[0][2]
        algtype = accountfetch[0][3]
        acc_1 = profile(username,email,emailtime,algtype)






        print("Your username is:", acc_1.getUsername())
        print("Your email is:", acc_1.getEmail())
        print("You will be sent an email at:", acc_1.getEmailTime())
        print("")
        print("""
        (1) Edit Clothing
        (2) Edit Profile
        (3) Reccomendation Now 
        (M) Starting Menu
        (C) Choose Account
        (X) Quit

        """)
        action = input("Choose your Option\n").lower()
        if action == "1":
            clothingdetailsoptions(acc_1)
            ans = True
            pass
        elif action == "2":
            profiledetails(acc_1)
            ans = True
            pass
        elif action == "3":
            #t.cancel()
            clear()
            prerec(acc_1)
            ans = True
            pass
        elif action == "m":
            #t.cancel()
            clear()
            starter()
            ans = True
            pass
        elif action == "c":
            #t.cancel()
            clear()
            chooseaccount()
            ans = True
            pass
        elif action == "x":
            raise SystemExit
            ans = True
            pass
        else:
            clear()
            profilemenu(acc_1)
            pass

    #t.join()
        

    #timertime is now how long the timer needs to be

    pass
#Gives options that even pass onto reccomendnow, profile details, clothing details, back to start choices or activates the reccomendation at a given time


def profiledetails(acc_1):
    ans = False
    while ans == False:

        c.execute("SELECT * FROM profiletable WHERE username LIKE :accountinput", {'accountinput': acc_1.username}) #lowercase stuff
        accountfetch = c.fetchall()
    
        #print(accountfetch)
        #stop = input("stop")

        username = accountfetch[0][0] 
        email = accountfetch[0][1]
        emailtime = accountfetch[0][2]
        algtype = accountfetch[0][3]
        acc_1 = profile(username,email,emailtime,algtype)





        clear()
        print("Your Profile details are:")
        print("")
        print("( 1 ) Username:", acc_1.username)
        print("( 2 ) Email:", acc_1.email)
        print("( 3 ) Time of Email:", acc_1.emailtime)
        print("( 4 ) Algorithm Type:", acc_1.algtype)
        print("( X ) Delete Account")
        print("( / ) Back to Menu")
        print("")

        action = input("What would you like to change?\n").lower()
        if action == "1":
            attribute = "username"
            clear()
            username = input("Enter new Username\n")
            c.execute("Select * FROM profiletable WHERE username =:username", {'username': username})
            checkusername = (str(c.fetchone()))
            #If check does not equal to none then that username must already exist in some form
            while checkusername != "None":
                username = input("That username is already in use, please choose another\n")
                username = input("Enter Username\n")
                c.execute("Select * FROM profiletable WHERE username =:username", {'username': username})
                checkusername = (str(c.fetchone()))
            #endwhile
            acc_1.setUsername(username)
            profiledetails(acc_1)
            pass
        elif action == "2":
            attribute = "email"
            clear()
            email = verification(attribute)
            acc_1.setEmail(email)
            pass
        elif action == "3":
            clear()
            timeformat = "%H:%M"
            inputtime = False
            while inputtime == False:
                
                emailtime = input("What time would you like your email? (hh:mm) \n")
                try: 
                    validtime = datetime.datetime.strptime(emailtime, timeformat)
                    inputtime = True
                except ValueError:
                    clear()
                    print("Not in the correct format, please try again")

            acc_1.setEmailTime(emailtime)
            profiledetails(acc_1)
            pass
        elif action == "4":

            clear()
            ex = False
            while ex == False:
                print("Which algorithm would you like to use?")
                print("( 1 ) Pure Clo - Arthur")
                print("( 2 ) Clo and Temp Range - Arthur")
                print("( 3 ) Clo - Josh")
                print("( / ) Back")
                selection = input("What would you like to do?\n").lower()
                if (selection == "1"): 
                    clear()
                    clo = "clo"
                    acc_1.setAlgType(clo)
                    profiledetails(acc_1)
                if (selection == "2"): 
                    clear()
                    clotr = "clotr"
                    acc_1.setAlgType(clotr)
                    profiledetails(acc_1)
                if (selection == "3"): 
                    clear()
                    cloj = "cloj"
                    acc_1.setAlgType(cloj)
                    profiledetails(acc_1)
                elif (selection == "/"):
                    clear()
                    profiledetails(acc_1)
                else:
                    clear()
                    print("This option cannot be selected")




            algtype = input("What Algorthim Type would you like?: Clo")
            acc_1.setAlgType
            #Add validation
            pass

        elif action == "x":
            clear()
            secexit = False
            while secexit == False:
                print("( X ) Are you sure? - Delete", acc_1.username)
                print("( / ) Back to Edit Item")
                selection = input("What would you like to do?\n").lower()
                if (selection == "x"): 
                    clear()
                    name = acc_1.username
                    acc_1.deleteself(name)
                    c.execute("Select username FROM profiletable")
                    clear()
                    starter()
                elif (selection == "/"):
                    clear()
                    profiledetails(acc_1)
                else:
                    clear()
                    print("This option cannot be selected")

        elif action == "/":
            clear()
            profilemenu(acc_1)
            pass
        else: 
            pass
        

    pass
#Shows profile details
#Allows user to change username, email, emailtime, algtype or to delete the account
#if account deleted - everything in database with that username must be deleted 
#User then would be passed back to start




def clothingdetailsoptions(acc_1):
    clear()
    exit = False
    while exit == False:

        ### Getting clothes
        c.execute ("Select clothingname from itemtable where username =:username", {'username': acc_1.username})
        
        firstclothingnamelist = (c.fetchall())
        lenoffirstclothingnamelist = len(firstclothingnamelist)
        secondlist = []
        optionlist = []
        for counter in range(lenoffirstclothingnamelist):
            optionlist.append(str(counter + 1))
            toadd = ("( " + str(counter + 1) + " ) " + firstclothingnamelist[counter][0])
            if toadd not in secondlist:
                secondlist.append(toadd)
            
        #Could make a function that sorts the items into category - for another time / not needed
    
        print("Clothing Library:")
        print(secondlist)
        rng = len(secondlist)

        print("( U ) DEVUpdateTR")
        print("( + ) Add New Item")
        print("( / ) Back to Main Menu")
        
        
        selection = input("Select an item to edit or delete\n").lower()
        check = checkaccount()
        if selection == "/":
            clear()
            profilemenu(acc_1)
        elif selection == "+":
            clear()
            additem(acc_1)
            clear()
        elif selection == "u":
            clear()
            devupdatetr(acc_1)
            clear()

        elif selection not in optionlist:
            clear()
            print("This number option cannot be selected")
            
        else:
            selection = int(selection) - 1
            item = str(firstclothingnamelist[selection][0])
            #print(item)
            #stop = input("stop")
            clear()
            clothingdetails(acc_1, item)

    
#Lists clothing and then: lets user pick a piece of clothing from that list - 

def devupdatetr(acc_1):
    name = acc_1.username
    c.execute("SELECT clothingname FROM itemtable WHERE username =:username", {'username': name}) #lowercase stuff
    items = c.fetchall()
    #print(items)
    lenofitems = (len(items))
    #stop = input("stop")

    for counter in range(lenofitems):
        opon = items[counter][0]
        #print(opon)
        c.execute("SELECT clothingtypekey FROM itemtable WHERE clothingname =:name", {'name': opon})
        ctk = c.fetchone()
        ctk = (ctk[0])
        c.execute("SELECT max, min FROM clothinginfotable WHERE clothingtypekey LIKE :clothingtypekey", {'clothingtypekey': ctk})
        temps = c.fetchall()
        #print(temps)
        temprangemax = temps[0][0]
        temprangemin = temps[0][1]
        #print(temprangemax)
        #print(temprangemin)

        #c.execute("SELECT * FROM itemtable WHERE clothingname =:item AND username = :username", {'item': item, 'username': acc_1.username}) #lowercase stuff
        #itemfetch = c.fetchall()
        clothingtypekey = ctk
        clothingname = opon
        username = name
        #print(item)
        #print(itemfetch)
        #stop = input("stop")
        #print(item)
        #print(itemfetch)
        #username = itemfetch[0][0] 
        #clothingname = itemfetch[0][1]
        #clothingtypekey = itemfetch[0][2]
        #temprangemin = itemfetch[0][3]
        #temprangemax = itemfetch[0][4]
        #cl_2 = clothing(username,clothingname,clothingtypekey,temprangemin,temprangemax)
        c.execute("""UPDATE itemtable SET temprangemax = :temprangemax
                    WHERE clothingname = :clothingname AND username = :username""",
                  {'temprangemax': temprangemax, 'clothingname': clothingname, 'username': username})
        conn.commit()
        c.execute("""UPDATE itemtable SET temprangemin = :temprangemax
                    WHERE clothingname = :clothingname AND username = :username""",
                  {'temprangemax': temprangemin, 'clothingname': clothingname, 'username': username})
        conn.commit()

def clothingdetails(acc_1, item):

    exit = False
    while exit == False:
        clear()

        c.execute("SELECT * FROM itemtable WHERE clothingname =:item AND username = :username", {'item': item, 'username': acc_1.username}) #lowercase stuff
        itemfetch = c.fetchall()
    
        #print(item)
        #print(itemfetch)
        #stop = input("stop")
        #print(item)
        #print(itemfetch)
        username = itemfetch[0][0] 
        clothingname = itemfetch[0][1]
        clothingtypekey = itemfetch[0][2]
        temprangemin = itemfetch[0][3]
        temprangemax = itemfetch[0][4]
        cl_2 = clothing(username,clothingname,clothingtypekey,temprangemin,temprangemax)
        #print(cl_2.username)
        #print(cl_2.clothingname)
        #print(cl_2.clothingtypekey)
        #stop = input("stop")



        print("For this piece of clothing:")
        print("")
        print("( 1 ) Edit Clothing Name:", cl_2.clothingname)
        print("( 2 ) Edit Clothing Type:", cl_2.clothingtypekey)
        print("( X ) Delete")
        print("( / ) Back to Clothing Library")
        print("")

        action = input("What would you like to do?\n").lower()
        if action == "1":
            clear()
            newname = input("What would you like the new item name to be?\n")
            cl_2.setClothingName(newname)
            item = newname
            clothingdetails(acc_1, item)
            clear()
            pass
        elif action == "2":
            clear()
            newtype = clothingtypechoosermenu(True)
            cl_2.setClothingTypeKey(newtype)
            clothingdetails(acc_1, item)
            clear()
            pass
        elif action == "x":
            clear()
            secexit = False
            while secexit == False:
                print("( X ) Are you sure? - Delete", cl_2.clothingname)
                print("( / ) Back to Edit Item")
                selection = input("What would you like to do?\n").lower()
                if (selection == "x"): 
                    clear()
                    name = cl_2.clothingname
                    cl_2.delete(name)
                    clothingdetailsoptions(acc_1)
                elif (selection == "/"):
                    clothingdetails(acc_1, item)
                else:
                    clear()
                    print("This option cannot be selected")
        elif action == "/":
            clear()
            clothingdetailsoptions(acc_1)
            pass
        else: 
            pass
        
    #t.join()


    pass
#Shows stuff about that particular piece of clothing
#User can then change the name or type of the clothing - depending on which decision is chosen, passes to different proc in class
#Or user has choice to delete the piece of clothing - again in class

def clothingtypechoosermenu(makeacc):
    exit = False
    #while exit == False:
    c.execute ("Select clothingtypecategory FROM clothinginfotable")
    firstlist = (c.fetchall())
    lenoffirstlist = len(firstlist)
    #print(lenoflist)
    #print(firstlist)
    #print("")
    #print(firstlist[0][0])
    secondlist = []
    for counter in range(lenoffirstlist):
        toadd = firstlist[counter][0]
        if toadd not in secondlist:
            secondlist.append(toadd)
        pass
    #print("End of New List Loop")
    #print(secondlist)
    #print(secondlist[0])
    print("Which category best describes your item?")
    while exit == False:
        lenofsecondlist = len(secondlist)
        optionlist = []
        for counter in range(lenofsecondlist):
            optionlist.append(str(counter + 1))
            print("(", counter + 1, ")", secondlist[counter] )    
        #print("( / )", "Exit")

        #print(lenofsecondlist)
        #print(secondlist[lenofsecondlist - 1])


        #optionlist = []
        #for counter in range(lenofsecondlist):
        #    optionlist.append(counter + 1)
        #print(optionlist)
        
        #STOP = input("STOP")

        #print(optionlist)

        selection = input()
        #selection = int(selection)
        if selection == "/":
            if makeacc == True:
                clear()
                print("You cannot exit to menu whilst entering in clothing for the first time, you can delete or edit accidental entries later, please complete this entry")
                print("Which category best describes your item?")
            else:
                clothingdetailsoptions()
                pass
        elif selection not in optionlist:
            clear()
            print("This number option cannot be selected")
            print("Which category best describes your item?")
        else:
            #print(selection)
            selection = int(selection) - 1
            #print(secondlist[selection])
            ctc = (secondlist[selection])

            ctk = clothingtypechoosersubmenu(ctc, makeacc)
            return ctk
            stop = input("stop")
        
def additem(acc_1):
    clothinglist = []
    end = False
    while end == False:
        makeacc = True
        cl_1 = enterclothing(acc_1.username, makeacc)
        c.execute("INSERT INTO itemtable VALUES (:username, :clothingname, :clothingtypekey, :temprangemin, :temprangemax)", {'username': cl_1.username, 'clothingname': cl_1.clothingname, 'clothingtypekey': cl_1.clothingtypekey, 'temprangemin': cl_1.temprangemin, 'temprangemax': cl_1.temprangemax})
        conn.commit()
        clear()
        clothinglist.append(cl_1.clothingname)
        inploop = True
        while inploop == True:
            print("You have entered ", clothinglist)
            ans = input("Another? (y/n)").lower()
            if ans == "y":
                end = False
                inploop = False
            elif ans == "n":
                end = True
                inploop = False
            else:
                clear()

def clothingtypechoosersubmenu(ctc, makeacc):
    clear()
    #print(ctc)
    c.execute("Select clothingtypekey FROM clothinginfotable WHERE clothingtypecategory =:ctc", {'ctc': ctc})
    submenufirstlist = (c.fetchall())
    lenoffirstlist = len(submenufirstlist)
    #print(submenufirstlist)
    
    submenusecondlist = []
    for counter in range(lenoffirstlist):
        toadd = submenufirstlist[counter][0]
        if toadd not in submenusecondlist:
            submenusecondlist.append(toadd)

    print("Which category in", ctc, "best describes your item?")
    exit = False
    while exit == False:
        lenofsecondlist = len(submenusecondlist)
        optionlist = []
        for counter in range(lenofsecondlist):
            optionlist.append(str(counter + 1))
            print("(", counter + 1, ")", submenusecondlist[counter] )    
        print("( / )", "Back to Clothing Categories")

        selection = input()

        if selection == "/":
            clear()
            clothingtypechoosermenu(makeacc)
        elif selection not in optionlist:
            clear()
            print("This number option cannot be selected")
            print("Which category in", ctc, "best describes your item?")
        else:
            #print(selection)
            selection = int(selection) - 1
            #print(secondlist[selection])
            ctk = (submenusecondlist[selection])
            #print(ctk)
            #stop = input("stop")
            return ctk

        #stop = input("stop")
        #pass
    return 
    
    pass


def reccomend(acc_1):
    
    #stop = input("STOP")
        #pt.terminate()
        #pass
    clear()

    met = 2.3 #metabolic rate in met
    # - This would be it for walking normally - clo value makes sense (cycling to work is 4.0 but because of energy made it skews result)
    #print("It worked")
    temp, adjtemp, wind = weatherget()
    #print("hi")
    #print(temp)
    #print(adjtemp)
    #print(wind)
    #print("bye")

    clovalue = clocalc(adjtemp, met)

    print(clovalue)

    stop = input("This is the Clo Value")

    print(adjtemp)

    stop = input("This is the adjusted temp")
    clear()
    JankAfButWorksForShow(acc_1, clovalue, adjtemp)
    profilemenu(acc_1)
    pass
#Contains the calls to functions to reccomend an outfit

def weatherget():
    observation = owm.weather_at_place('London,GB')
    w = observation.get_weather()
    wind = w.get_wind()
    temp = w.get_temperature('celsius')
    #print(w)
    #print(wind)
    #print(temp)
    wind = wind.get('speed')
    temp = temp.get('temp')
    #print(wind)
    wind = 3.6*wind


    #print(wind)
    #stop = input("stop")

    #print(temp)
    

    ### - Adjust for wind chill
    if temp >= 4.8:
        #temp = -20
        #wind = 5
        adjtemp = 13.12+(0.6125*temp)-(11.37*(wind**0.16))+(0.3965*temp)*(wind**0.16)
    else:
        adjtemp = temp
        #one = (13.12+(0.6125(temp)))
        #two = pow((11.37(wind), 0.16))
        #print(adjtemp)
        pass
    return temp, adjtemp, wind;
    ### - A


    pass
#gets values for windspeed and temperature
#if windspeed > certain amount then find windchill to get adjusted temp
#else adjustedtemp = temperature 

def clocalc(temp, met):

    ###
    #activitylevel = 60
    #clo = abs((temp - 31)/(0.155*activitylevel))
    ###

    #1 Met = 58W/m^2 - cycling = 4 met
    watt = met*52

    
    clo = abs((temp - 31)/(0.155*watt))
    
    
    return clo

    pass
#calculates the clovalue that would be needed for the adjusted temperature

def JankAfButWorksForShow(acc_1, clovalue, adjtemp):

    # This probably won't work on a RPI cos of puny memory limit 
    # This needs to be changed to a non hardcoded flexible list thing in a dictionary - so if ctcs are added, don't have to change code
    # Also use proper joins - am tired (fix sunday morning)

    UnderwearBottom = []
    UnderwearTop = []
    Shirts = []
    Trousers = []
    CoverallsOveralls = []
    Sweaters = []
    CoatJacket = []
    Socks = []
    Shoes = []
    Skirts = []
    Dresses = []

    username = acc_1.username
    c.execute("Select * FROM itemtable WHERE username =:name", {'name': username})
    useritems = (c.fetchall())
    #print(useritems)
    #stop = input("stop")
    clear()
    lenuseritems = len(useritems)
    #print(lenuseritems)
    #stop = input("stop")
    for counter in range(lenuseritems):
        currentitemname = useritems[counter][1]
        #print(currentitemname)
        #stop = input("stop")
        ctk = useritems[counter][2]
        c.execute("Select clothingtypecategory FROM clothinginfotable WHERE clothingtypekey =:ctk", {'ctk': ctk})
        category = (c.fetchone())
        category = category[0]
        #print(category)
        #stop = input("stop")
        if category == "Underwear (Bottom)":
            UnderwearBottom.append(currentitemname)
            #pass
        elif category == "Underwear (Top)":
            UnderwearTop.append(currentitemname)
            #pass
        elif category == "Shirts":
            Shirts.append(currentitemname)
            #pass
        elif category == "Trousers":
            Trousers.append(currentitemname)
            #pass
        elif category == "Coveralls/Overalls":
            CoverallsOveralls.append(currentitemname)
            #pass
        elif category == "Sweaters":
            Sweaters.append(currentitemname)
            #pass
        elif category == "Coat/Jacket":
            CoatJacket.append(currentitemname)
            #pass
        elif category == "Socks":
            Socks.append(currentitemname)
            #pass
        elif category == "Shoes":
            Shoes.append(currentitemname)
            #pass
        elif category == "Skirts, dresses":
            Skirtsdresses.append(currentitemname)
        elif category == "Skirts, dresses":
            Skirtsdresses.append(currentitemname)
            #pass

    UnderwearTop.append("None")
    CoverallsOveralls.append("None")
    Sweaters.append("None")
    CoatJacket.append("None")
    Skirts.append("None")
    Dresses.append("None")

    #print(Sweaters)
    #print(Sweaters[0])
    combolist = []
    combolist.append(UnderwearBottom)
    combolist.append(UnderwearTop)
    combolist.append(Shirts)
    combolist.append(Trousers)
    combolist.append(CoverallsOveralls)
    combolist.append(Sweaters)
    combolist.append(CoatJacket)
    combolist.append(Socks)
    combolist.append(Shoes)
    combolist.append(Skirts)
    combolist.append(Dresses)

    #print(combolist)
    #stop = input("before")

    r=[[]]
    for x in combolist:
        t = []
        for y in x:
            for i in r:
                t.append(i+[y])

        r = t

    #id = 0
    #lencomblist = len(r)
    #for fcounter in range(lencomblist):
    #    possiblecombo = r[fcounter]
    #    posscomblen = len(possiblecombo)
    #    id = id + 1
    #    totalclo = 0
    #    for tcounter in range(posscomblen):
    #        itemforclosearch = r[fcounter][tcounter]
    #        print(itemforclosearch)
    #        try:
    #            uname = acc_1.username
    #            c.execute("Select clothingtypekey FROM itemtable WHERE clothingname =:name AND username =:uname", {'name': itemforclosearch, 'uname': uname})
    #            ctk = c.fetchone()
    #            ctk = ctk[0]
    #            c.execute("Select clovalue FROM clothinginfotable WHERE clothingtypekey =:ctk", {'ctk': ctk})
    #            cvalue = c.fetchone()
    #            cvalue = cvalue[0]
    #            totalclo = totalclo + cvalue
    #        except:
    #            pass
    #    #clear()
    #    #print(id)
    #    #print(totalclo)
    #    #stop = input("stop")
    #    r[counter] = [id] + r[counter]
    #    r[counter].append(totalclo)

    
    lenoflist = len(r)
    id = 0
    #Iterates through all the combinations 
    for fcounter in range(lenoflist):
        #Total appropriatness points (which will be averaged by amount of non-none items
        app = 0
        #Total unsuitability points (which will be averaged by amount of non-none items
        inapp = 0
        #Averaged appropriatness points minus unsuitability points
        apptotal = 0
        #Standard Deviation of the median temperature range values for the items 
        std = 0
        #List for the median temp range values of each item 
        med = []

        iteminrec = 0

        #Total clo from all seperate values
        totalclo = 0
        #For primary key random identificaiton sorting whatever
        id = id + 1


        combo = (r[fcounter])
        lenofcombo = len(combo)

        #Iterates through the items in that combo
        for tcounter in range(lenofcombo):
            item = (r[fcounter][tcounter])
            #checks if there is an item in that category - if there is then it is operated on
            if item != 'None' or None:
                iteminrec = iteminrec + 1
                #Username will be used when searching sqltable for correct clothing type key
                uname = acc_1.username
                c.execute("Select clothingtypekey FROM itemtable WHERE clothingname =:name AND username =:uname", {'name': item, 'uname': uname})
                ctk = c.fetchone()
                ctk = ctk[0]
                #Clo value selected from the item will be used to add to the total clo value of that combo
                c.execute("Select clovalue FROM clothinginfotable WHERE clothingtypekey =:ctk", {'ctk': ctk})
                cvalue = c.fetchone()
                cvalue = cvalue[0]
                totalclo = totalclo + cvalue

                #I need to find the max and min temp range values - if max value is "none" then make it 35, if min value is "none" then make it -15
                c.execute("Select temprangemin, temprangemax FROM itemtable WHERE clothingname =:name AND username =:uname", {'name': item, 'uname': uname})
                temps = c.fetchall()

                #print(temps)
                #stop = input("stop")


                trmax = str(temps[0][0])
                trmin = str(temps[0][1])

                if trmax == "None":
                    trmax = 35
                if trmin == "None":
                    trmin = -15
                trmax = int(trmax)
                trmin = int(trmin)


                #If the current temperature is within the boundaries then appropriateness is increased by appropriatness + 0.1
                #If outside the range then inappropriatness = inappropriatness + 0.1
                if adjtemp <= trmax and adjtemp >= trmin:
                    app = app + 0.1
                else:
                    inapp = inapp + 0.1
                #need to append the midpoint between the two boundaries to the med list
                entrytomed = trmax+trmin
                entrytomed = entrytomed/2
                med.append(entrytomed)
            else:
                #If the item is equal to none then it skips that part
                pass


        #Need to average app and inapp based on how many clothing items are not none in that combo

        app = app/iteminrec
        inapp = inapp/iteminrec


        #then subtract inapp from app to make an avg adj total app

        adjapp = app - inapp

        #Append this adjusted app value to the list
        #Do standard deviation on the med list and also append that to the list
        std = statistics.pstdev(med)


        r[fcounter].insert(0,id)
        r[fcounter].append(totalclo)
        r[fcounter].append(std)
        r[fcounter].append(adjapp)

    clear()

    #print (r)
    #print (len(r))
    
    #print(r[0])

    #stop = input("stop")

    clear()

    
    









    ################################################################################################################################################################################################################################################

    # All the Combos will now have (adj avg app total), (STD value), (Clo value)

    # Iterate through the lists and do hard coded logic on which pairings are stupid and deleted them
    
    # Then iterate through the lists and sort them into 3 lists, - one ordered by the highest app total, one by the lowest std value, and one for the closest clo value 

    # Then make a nested list with each combo id and the places it got on the lists

    # Make a final list that has the id and averaged placement from the three lists ordered

    # Best possible choice should be one of the top selection (lowest value, since higher placement means closer to one)

    # Note to self - totalclo is the 12th value, standard deviation is the 13th value and adjapp is the 14th value




    #Sort by 

    adjapplist = r
    totalclolist = r
    stdlist = r















    adjapplist = sorted(adjapplist, key=lambda x: x[14])
    
    #print(adjapplist)

    stdlist = sorted(stdlist, key=lambda x: x[13])

    totalclolist = sorted(totalclolist, key=lambda x: x[12])



    stop = input("stop")

    stop = input("stop")
    lenofsort = len(r)
    placements = []
    for counter in range(lenofsort):
        ccplacements = []
        #The Combo ID [counter][0]
        id = r[counter][0]
        ccplacements.append(id)

        TC = r[counter][12]


        #TheTotalClo [counter][1]
        ccplacements.append(TC)
        #STD [counter][2]
        ccplacements.append(SD)
        #SDJAPP [counter][3]
        ccplacements.append(AA)

        #appendsthatcomboslisttotheplacementlist
        placements.append(ccplacements)



        pass

















    ################################################################################################################################################################################################################################################

    ##### The following will put all those combinations in a created table which will be deleted after                          ######(remember to use range values)######


    c.execute("""
    CREATE TABLE combinationtable
    (
    combinationdid integer,
    UnderwearBottom text,
    UnderwearTop text,
    Shirts text,
    Trousers text,
    CoverallsOveralls text,
    Sweaters text,
    CoatJacket text,
    Socks text,
    Shoes text,
    Skirts text,
    Dresses text,
    clovaluetotal integer
    )
    """)
    conn.commit()

    


    for counter in range(lenoflist):
        
        c.execute("INSERT INTO combinationtable VALUES (:combinationdid, :UnderwearBottom, :UnderwearTop, :Shirts, :Trousers, :CoverallsOveralls, :Sweaters, :CoatJacket, :Socks, :Shoes, :Skirts, :Dresses, :clovaluetotal)", {'combinationdid': r[counter][0], 'UnderwearBottom': r[counter][1], 'UnderwearTop': r[counter][2], 'Shirts': r[counter][3], 'Trousers': r[counter][4], 'CoverallsOveralls': r[counter][5], 'Sweaters': r[counter][6], 'CoatJacket': r[counter][7], 'Socks': r[counter][8], 'Shoes': r[counter][9], 'Skirts': r[counter][10], 'Dresses': r[counter][11], 'clovaluetotal': r[counter][12]})
        conn.commit()

    print(adjtemp)
    stop = input("befdel")

    min = 0.9 * clovalue
    max = 1.1 * clovalue
    c.execute("DELETE FROM combinationtable WHERE clovaluetotal NOT BETWEEN :min AND :max", {'min': min, 'max': max})
    conn.commit()

    stop = input("aftdel")


    c.execute("DROP TABLE combinationtable")
    conn.execute("VACUUM")
    conn.commit()

    stop = input("chk")

    ##### End of SQL jankiness


        #print(currentitemname)
        #stop = input("stop")


    # first put all ctks in the correct ctcreflist

    #### Sample
    ##underwearpantsref = [1]
    ##lists = [underwearpantsref]
    ##first = lists[0]
    ##print(first)
    ##stop = input("stop")
    ##first[0] = 2
    ##print(underwearpantsref)
    ##stop = input("stop")


    ###Basicallllllly - the idea is that the cts are not hardcoded so if you change the database/excel to add another ctc you dont need to worry about the code

    #listtest = []
    #newlctc = "first"
    #newlctc = newlctc[]

    #listtest.append(first)
    #listtest[0,0] = 1
    #print(listtest)
    #stop = input("stop")

    #underwearpantsref = []
    #underwearshirtsref = []
    #shirts = []
    #trousers = []
    #coveralls = []
    #highinscoveralls = []
    #sweaters = []
    #jacket = []
    #coatsoverjacketsovertrousers = []
    #socks = []
    #shoes = []
    #skirtsdressers = []
    #sleepwear = []
    #robes = []

    #c.execute("Select * FROM clothinginfotable")
    #listofinfotable = (c.fetchall)
    #print(listofinfotable)



    #c.execute("Select clothingtypekey FROM clothinginfotable WHERE clothingtypecategory =:ctc", {'ctc': ctc})
    #submenufirstlist = (c.fetchall())
    #lenoffirstlist = len(submenufirstlist)


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
#print("Table made")
#comment out tablemaker after first run

def test():
    # Basic logic for getting t
    

    name = "SpencerA"
    item = "Boxers"
    c.execute("Select temprangemin, temprangemax FROM itemtable WHERE clothingname =:name AND username =:uname", {'name': item, 'uname': name})
    ctk = c.fetchall()
    trmax = ctk[0][0]
    trmin = ctk[0][1]
    print("Temprangemaxis: " + str(trmax))
    print("Temprangeminis: " + str(trmin))
    if trmax == "":
        trmax = 1000
    if trmin == "":
        trmin = -1000
    print("max")
    print(trmax)
    print("min")
    print(trmin)
    stop = input("stop")
    pass

def test2():
    name = ("Tube top")
    c.execute("Select max, min FROM clothinginfotable WHERE clothingtypekey =:name", {'name': name})
    temps = c.fetchall()
    print(temps)
    none = (temps[0][0])
    print(none)
    print(str(none) + "hello")
    stop = input("stop")

#def dicttest():
    #Theory - sort r list into 3 lists - one ordered by smallest difference to targetclo, one ordered by highest adjapp and one ordered by lowest std
    #Go through the sorted lists
    #At the beginning placement = 1 - go from top of list to bottom of the list
    #When you go to the next value, if it is different from the previous value, placement = placement + 1 -- (otherwise it is tied and it will be given the same placement)
    #On the first loop just add a key/value for each if 
    #on the third and second loop just add values to the keys that already exist
    #Then you can iterate through each key in the list and make an average of the three values which is appended to make a 4th value to the key
    #Then i need to find a way of making a list out of the key (the id) and the 4th (averaged value)
    #Then i can sort through the list by the averaged placement value and see which if is at the top
    #Then see what i can do from there


    #(Idea for implementing a colour factoring - You have a list of the combo ids and at the top should be the ones which are: closest to clo value, most appropriate, have the least variation
    #User should be able to choose whether they want to algorithm to test for colour preference/ palette
    #2 algorithms - one without colour, one which takes colour preferences into consideration
    #If the colour adjusted alg option is selected then:
    #



#test()
#test2()
#dicttest()



t = False
while t != True:
    starter()
    print("You got out")
else:
    reccomend(acc_1)
###
### Main calling program - hopefully should never be broken out of, because all functions refer to different functions - they dont refer to self so hopefully no stack overflow recursion errors 
