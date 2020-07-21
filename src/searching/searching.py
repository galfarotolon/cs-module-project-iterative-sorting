def linear_search(arr, target):
    # Your code here
    # check all elements in the array one by one, and compare them with the target value
    for i in range(len(arr)):
        # if the value checked is the same as target, return it 
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
#returns either the index of the target in the arr
# or a -1 if the target is not in the arr

def binary_search(arr, target):

    # the 'range': left-most inde and right-most index
    low = 0
    high = len(arr) - 1
    
    while low <= high:

    # 1. compare the target element to the midpoint
     # then midmoint element is right index + left index / 2
        mid = (high + low) // 2 #double dash is to automatically floor the value

        # 2. determine which half to go in; discard the other half
            #reassign either left or right index to point to the element past the midpoint
        
              # 3. if the midpoint element matches target, then we've
        # found the target we are looking for, return midpoint index
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            #cut right half 
            # in this case, reassign high to mid -1
            high = mid - 1
        if target > arr[mid]:
            # cutt off the left half
            # reassign low to mid +1 
            low = mid + 1
    
         # how do we find the midpoint? what do we need  to know?
       
        #4. repeat: loop this 
            # what is looping criteria? what tells us that we're done looping

            # if we see that the low and high are the same index,
            # and the element is not the target, then the element is not in the array,
            # return -1

            # when low and high meet, that is when we can stop looping
    return  -1 