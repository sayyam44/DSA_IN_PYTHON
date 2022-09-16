# https://leetcode.com/problems/next-greater-element-i/
# https://www.youtube.com/watch?v=Du881K7Jtk8&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=76
# For the input array [4, 5, 2, 25]
# output===Element       NGE
        #    4      -->   5
        #    5      -->   25
        #    2      -->   25
        #    25     -->   -1

 # same as daily temperature ques 
 def nge(arr,n):
    res=[-1]*n
    s=[]

    for i,t in enumerate (arr):
        while s and t>s[-1][0]:
            sT,sI=s.pop()
            res[sI]=t
        s.append([t,i])
    return res

 # /* if stack is not empty, then
        # pop all the elements from stack that are smaller than arr[i]
        # Add arr[i] into the result at ith position 
        # Add arr[i] INTO THE STACK 
#tc=n+n(reason below) , sc=n ,THIS IS FOR STRAIGH SINGULAR ARRAY
def nge(arr,n):
    s=[]
    res=[0 for i in range(n)]

    for i in range(n-1,-1,-1):
        if len(s)!=0:
            while len(s)!=0 or arr[i]>=s[-1]:
                s.pop()
        res[i]=-1 if len(s)==0 else s[-1]
        s.append(arr[i])  

    return res      

#  FOR CIRCULAR ARRAY
# we will assume the same array infront of the original array for cmaking it look like circular 
# in order to get the same index as the 1st half (original) array , without actually doing the 1st step  we will do i%n everywhere 
# tc=2n+2n , because for loop will move for ntimes whereas whiel loop will not always move for n times
# sc=n , because we dont count sc for the space that we used to compute the output i.e. space for res is not counted 
def nge(arr,n):
    s=[]
    res=[0 for i%n in range(n)]

    for i in range(2n-1,-1,-1):
        if len(s)!=0:
            while len(s)!=0 or arr[i%n]>=s[-1]:
                s.pop()
        res[i%n]=-1 if len(s)==0 else s[-1]
        s.append(arr[i%n])  

    return res  

#question in leetcode

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int])->List[int]:
        if not nums2: return None

        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        #finding the next greater element for nums2 following same old process
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:       # if stack is not empty, then compare it's last element with nums2[i]
                #in mapping we are not putting the difference instead we are putting the actual greater element
                mapping[stack[-1]] = nums2[i]           # if the new element is greater than stack's top element, then add this to dictionary 
                stack.pop()                             # since we found a pair for the top element, remove it.
            stack.append(nums2[i])                      # add the element nums2[i] to the stack because we need to find a number greater than this

        for element in stack:                           # if there are elements in the stack for which we didn't find a greater number, map them to -1
            mapping[element] = -1

            
        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result



