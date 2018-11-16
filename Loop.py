search_list = [5,8,13,7,6,9,3,1]

search_item = int(input("enter number:"))

def linear_search(sl,si):
    found_index = -1

    for index in range (len(sl)):
        if sl[index] == si
            found_index = index
        #end if
    #next
    return found_index

def linear_search2[sl,si]
    index = 0
    found_index = -1
    found = False
    while not found and index < len(sl):
        if sl[index] == si:
              found_index = index
              found = True 
            #end if
            index = index + 1
    #end while
    return found_index
#end function

search_list = [5,8,13,7,6,9,3,1]
print (search_list)
search_item = int(input("Enter Number:"))

if found_index 1= -1:
    print("found at index:", found_index)
else:
    print("not found")
#end if

print (search_list)
