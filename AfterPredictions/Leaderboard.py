import json
import os
import sys
clear = lambda: os.system('cls')

def menu():
    with open('leader_board.txt') as json_data:
        lb = json.load(json_data,)
        
    exit = False
    while exit == False:
        
        print("""
    Leaderboard

        ( 1 ) Add Enteries
        ( 2 ) Load Leaderboard
        ( 3 ) Exit
        """)
        selection = input("    What would you like to do?\n")
        if (selection == "1"):
            clear()
            new()
        elif (selection == "2"):
            clear()
            load()
        elif (selection == "3"):
            clear()
            exit()
        else:
            print("This number option cannot be selected")

def new():
    exit = False
    while exit == False:
        name = input("Enter Name ")
        score = input("Enter Score ")
        lb[name] = score
        check = input("Another Entry? y/n ").lower()
        if check == "n":
            with open('leader_board.txt', 'w') as outfile:  
                json.dump(lb, outfile)
            menu()

def insertionsort(lblist):
    n=len(lblist)
    for index in range(1, n):
        rep = lblist[index]
        currentvalue = lblist[index][1]
        position = index
        while position > 0 and (lblist[position - 1][1]) > currentvalue:
            lblist[position] = lblist[position - 1]
            position = position - 1
        lblist[position] = rep
    return lblist     

def load():
    lblist = []
    for x in lb:
        y = []
        y.append(x)
        y.append(lb[x])
        lblist.append(y)
    newlb = insertionsort(lblist)
    newlb = (newlb[::-1])
    x = len(newlb)
    for i in range(x):
        print(newlb[i])
    x = input("Press any key to continue")
    clear()
    menu()

try:
    with open('leader_board.txt') as json_data:
        lb = json.load(json_data,) 
    menu()
except:
    lb = dict()
    menu()
