def recbin(li, find, first, last):
    
    mid = int((first + last)/2)
    #print(mid)
    #print(li[mid])
    if find > li[mid]:
        first = mid
        recbin(li, find, first, last)
    elif find < li[mid]:
        last = mid
        recbin(li, find, first, last)
    elif find == li[mid]:
        print (li[mid])
        print ("at (starting at 0)")
        print (mid)
        
    else:
        print ("not present")
        return -1
    #endif
        
    
#li = [1,2,3,4,5,6,7,8]
li = [2,5,6,7,9,10,15,17,18,19]
print (li)
find = 7
first = 0
last = (len(li) - 1)
recbin(li, find, first, last)
