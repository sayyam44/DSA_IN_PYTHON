# https://leetcode.com/problems/product-of-array-except       -self/
def productExceptSelf(nums):
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]
    res=[1]*len(nums) #creating an array with all elements as 1 ,equal to the length of the given list

    prefix=1
    for i in range(len(nums)):
        res[i]=prefix #giving the current res value as the prefix value    
        prefix*=nums[i] #prefix = previous prefix *current value that will be used for the next element in res
    
    postfix=1
    for i in range(len(nums)-1,-1,-1): #iterating from the back of list
        res[i]*=postfix  #giving the current res value (which already contains the prefixes values) multiplying with postfix values
        postfix*=nums[i] #postfix = previous postfix *current value that will be used for the next element in res
    return res
        