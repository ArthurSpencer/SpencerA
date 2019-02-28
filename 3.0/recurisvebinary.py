def bin(li, search, mid):
    le = len(search) - 1
    if le >= 1:
        mid = 1 +(le - 1)/2

        if list[mid] == x:
            return mid

        elif list[mid] > x:
            
            return bin(li, search, mid - 1)
        else:
            return bin(li, search, mid +1)
        #endif
#endfunction


mid = 0
li = [0,1,2,3,4,5,6,7,8]
print(bin(li, 7, mid))
