def linearsearch(alist, itemsought, start):
    index = -1
    i = start
    found = False
    while i < len(alist) and found == False:
        if alist[i] == itemsought:
            index = i
            found = True
        #endif
        i = i + 1
    #endwhile
    return index
#endfunction

alist = [3, 5, 1, 7, 2, 16, 0, 2, 17]

i = 0
end = False
while i < len(alist) and end == False:
    location = linearsearch(alist, 2, i)
    if location != -1:
        print(location)
    i = location
    if i == -1:
        end = True
    i = i + 1
    
    
