def recbin(li, find, first, last):
    
    mid = int((first + last)/2)
    print(mid)
    print(li[mid])
    if find > li[mid]:
        first = mid
        recbin(li, find, first, last)
    if find < li[mid]:
        last = mid
        recbin(li, find, first, last)
    if find == li[mid]:
        return li[mid]
    else:
        return -1
    
li = [1,2,3,4,5,6,7,8]
find = 7
first = 0
last = (len(li) - 1)
recbin(li, find, first, last)
