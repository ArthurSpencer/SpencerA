def calc(n):
    if n > 0:
        n = n + calc(n - 1)
    print(n)
#endfunction
n = 5
calc(n)
print(n)
