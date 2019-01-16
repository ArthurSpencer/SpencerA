import time
startTime1 = time.clock()
def fib2(n):
    fibnumbers = [0,1]
    # now append the sum of the two previous numbers to the list
    for i in range (2, n):
        fibnumbers.append(fibnumbers[i-1] + fibnumbers[i-2])
    #next
    return fibnumbers
#endfunction
n = 20
fib2(n)
endTime1 = time.clock()
print(endTime1)
