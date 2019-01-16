import time
startTime1 = time.clock()
def fib(n):
    if n<= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))
    #endif
#endfunction
n = 20
fib(n)
endTime1 = time.clock()
print(endTime1)

