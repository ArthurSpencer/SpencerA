listofnodes = []
initialstate = [["-",1,3],
                [4,2,5],
                [7,8,6]]

currentstate = initialstate

goalstate = [[1,2,3],
             [4,5,6],
             [7,8,"-"]]


def incorrectfinder(currentstate):
    incorrect = 0
    for i in range(3):
        for u in range(3):   
            if currentstate[i][u] != goalstate[i][u]:
                incorrect = incorrect + 1
    return incorrect

# Node = [layout, incorrectpositions, distancefromstart, totalheuristic, previousnodeindex]

node = [currentstate, incorrectfinder(currentstate), 0]
node.append(-1)
node.append(-1)
listofnodes.append(node)
currentnode = 0

# u = x
# i = y

found = False
while found == False:
    # Find new nodes
    # First find position of - in currentstate
    for i in range(3):
        for u in range(3):
            if currentstate[i][u] == '-':
                dashposition = [i,u]
    # print(dashposition)

    # To the left
    try:
        check = dashposition[1] - 1
        if check < 0:
            x = 5/0
        print(currentstate[dashposition[0]][check])

        editedstate = currentstate
        editedstate[dashposition[0]][check] = '-'
        editedstate[dashposition[0]][dashposition[1]] = currentstate[dashposition[0]][check]
        print(editedstate)
        
    except:
        pass
    
    #To the right
    try:
        check = dashposition[1] + 1
        if check > 2:
            x = 5/0
        #print(currentstate[dashposition[0]][check])
        editedstate = currentstate
        editedstate[dashposition[0]][check] = '-'
        editedstate[dashposition[0]][dashposition[1]] = currentstate[dashposition[0]][check]
        print(editedstate)
    except:
        pass
    
    # To the top
    try:
        check = dashposition[0] - 1
        if check < 0:
            x = 5/0
        #print(currentstate[check][dashposition[1]])
    except:
        pass
    
    #To the bottom
    try:
        check = dashposition[0] + 1
        if check > 2:
            x = 5/0
        #print(currentstate[check][dashposition[1]])
    except:
        pass

    
    
    

