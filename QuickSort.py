import random

def partition(alist, start, end):
    i = start - 1
    pivot = alist[end]
    for j in range(start,end):
        if alist[j] <= pivot:
            i = i+1
            alist[i],alist[j] = alist[j], alist[i]
    alist[i+1],alist[end] = alist[end], alist[i+1]
    return(i+1)

def quicksort(alist, start, end):
    if start < end:
        split = partition(alist, start, end)
        quicksort(alist, start, split - 1)
        quicksort(alist, split + 1, end)

alist = [random.randint(0,10) for i in range(10)]
print(alist)
n = len(alist)
quicksort(alist, 0, n-1)
print(alist)
