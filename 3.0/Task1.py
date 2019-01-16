def addEvens(first, maxn, tot):
    tot = tot + first
    if first < maxn:
        addEvens(first + 2, maxn, tot)
    else:
        print(tot)
    #endif
#endprocedure
tot = 0
first = 0
rep = True
while rep == True:
    maxn = int(input("what is the even upper boundary\n"))
    if maxn % 2 == 0:
        rep = False
    #endif
#endwhile
addEvens(first, maxn, tot)
