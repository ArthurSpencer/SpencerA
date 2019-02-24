x = False
def bubblesort(nums):
    for j in range (0,len(nums)-1):
        if x == True:
            x = False
            for j in range(0,len(nums) - 1): 
                for i in range ((0,len(nums) - 2 - j)):
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        x = True
                    #Endif
                #next
            #next
        #endif
        return nums
#endfunction
nums=[9,5,4,15,3,8,11]
print(bubblesort(nums))

    
