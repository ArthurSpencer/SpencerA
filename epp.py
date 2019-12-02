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

found = False
while found == False:
    # Find new nodes
    # First find position of - in currentstate
    for i in range(3):
        for u in range(3):   
            if currentstate[i][u] == '-':
                dashposition = [i,u]
    print(dashposition)
    
    

