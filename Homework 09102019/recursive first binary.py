alist = [1, 2, 2, 2, 2, 3, 5, 7, 16, 17]
# Should be index 1

def binarysearch(alist, itemsought, first, last):
    if last < first:
        return -1
    else:
        midpoint = int((first+last)/2)
        if alist[midpoint] > itemsought:
            return binarysearch(alist, itemsought, first, midpoint - 1)
        elif alist[midpoint] < itemsought:
            return binarysearch(alist, itemsought, midpoint + 1, last)
        elif first != midpoint:
            return binarysearch(alist, itemsought, first, midpoint)
        else:
            return midpoint
        #endif
    #endif
#endfunction

print(binarysearch(alist, 2, 0, len(alist)))        
            
