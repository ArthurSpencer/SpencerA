def insertionsort(alist):
    n=len(alist)
    for index in range (1, n - 1):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
        #endwhile
        alist[position] = currentvalue
#endprocedure

#Main Program
alist=[9,5,4,15,3,8,11]
insertionsort(alist)
print("sorted list ", alist)
