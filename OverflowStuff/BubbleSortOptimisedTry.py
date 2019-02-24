def bubblesort(numbers):
    i = -1
    numItems = len(numbers)
    flag = True
    while i < (numItems - 1) and (flag == True):
        flag = False
        for j in range (0,numItems - i - 2):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
                flag = True
            #endif
        #next
    #endwhile
    print(numbers)
#endfunction
numbers = [9,5,4,15,3,8,11]
print(bubblesort(numbers))
    
