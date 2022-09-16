# https://www.youtube.com/watch?v=LuLCLgMElus&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=10
# https://leetcode.com/problems/next-permutation/solution/

def nextPermutation(arr):
    # Input: nums = [1,2,3]
    # Output: [1,3,2]
    """
    Do not return anything, modify nums in-place instead.
    """
    #tc=n+n+n=n, sc=1
    #start trasversing i from back
    # [1,3,5,4,2] 
    # a[i]<a[i+1] a[i]=3 (1st decreasing element) 
    # now again start trasversing from end and find a[i]>3 here i.e.= 4
    #now swap 3 with 4
    #[1,4,5,3,2]
    # now reverse all the elements from behind till 4.
    #[1,4,2,3,5]
    
    
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]: #(1st decreasing element)
        i -= 1
    if i <= 0:
        return False

    # Find a numbers just greater than the above 1st dec element
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    
    return True

    #another method in leetcode (both are same )