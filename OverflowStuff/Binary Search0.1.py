def binarySearch(aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList)-1
    while first <= last and found != last:
        midpoint = (first + last) % 2
        if aList(midpoint) == itemSought:
            found = aList(midpoint)

        
        elif aList(midpoint)<itemSought:
                first = aList(midpoint)
        else:
                last = aList(midpoint)
            #endif
        #endif
    #endwhile
    return index
#endfunction

aList = [0,1,2,3,4,5,6,7]
itemSought = 3
binarySearch (aList,itemSought)        
