alist = [1, 2, 2, 2, 2, 3, 5, 7, 16, 17]
# Should be index 1

def binarysearch(alist, itemsought):
    found = False
    index = -1
    first = 0
    last = len(alist)-1
    while first <= last and found == False:
        midpoint = int((first + last)/2)
        if alist[midpoint] < itemsought:
            first = midpoint + 1
        elif alist[midpoint] > itemsought:
            last = midpoint - 1
        elif first != midpoint:
            last = midpoint
        else:
            found = True
            index = midpoint
        #endif
    #endwhile
    return index
#endfunction


print(binarysearch(alist, 2))
