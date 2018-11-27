def bubblesort(nums):
    numitems = len(nums)
    number = numitems - 1
    flag = True
    while number > 0:
        flag = False
        for i in range(number):
            if nums[i] > nums[i+1]:
                flag = True
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
            #endif
        #next
        number = number - 1
    #endwhile
    print(nums)
#endfunction
nums=[9,5,4,15,3,8,11]
print (nums)
print(bubblesort(nums))
