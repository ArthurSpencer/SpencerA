def binarysearch(alist,itemsought):
    found = False
    index = -1
    first = 0
    last = len(alist)-1
    while first <= last and found == False:
        midpoint = int((first + last)/2)
        if alist[midpoint] == itemsought:
            found = True
            index = midpoint
        else:
            if alist[midpoint] < itemsought:
                first = midpoint + 1
            else:
                last = midpoint - 1
            #endif
        #endif
    #endwhile
    print(index)
#endfunction 

alist = [0,1,2,3,4,5,6,7]
itemsought = 3
binarysearch(alist,itemsought)        
