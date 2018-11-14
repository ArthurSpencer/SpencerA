

numlist = [7,6,3,1,18,23,2,100]
alphalist = ['A','C','D','G','M','R','W','Z']

def linearsearch(alist,itemsought):
    index = -1
    i = 0
    found = False
    while i < len(alist) and not found:
        if alist[i] == itemsought:
            index = i
            found = True
        #endif
        i = i + 1
    #endwhile
    return index
#endfunction



print(linearsearch(numlist,1))
print(linearsearch(numlist,4))
print(linearsearch(alphalist,'M'))
print(linearsearch(alphalist,'N'))
