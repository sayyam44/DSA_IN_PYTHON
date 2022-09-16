# https://www.youtube.com/watch?v=w_KEocd__20&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=6
# https://leetcode.com/problems/maximum-subarray/
def maxSubArray(nums):
#    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#    Output: 6
#    Explanation: [4,-1,2,1] has the largest sum = 6.

    #kadane's algorithm(in copy)
    #optimized solution
    #tc=n,sc=1
   
    s = 0
    max_sum = nums[0]
    for i in range(len(nums)):
        s+=nums[i]
        if s<0:
            s = 0 #sum with negative value will be of no use in finding the max sum so make it = 0if it is<0
        max_sum = max(max_sum,s)   
    return max_sum

  #brute-force method
        #tc=n2,sc=n
        
#         if len(nums)==1:
#             return nums[0]
        
#         add=0
#         lst=[]

#         for i in nums:
#             lst.append(add)
#             for j in nums[i+1:]:
#                 add=i+j
#                 lst.append(add)  
#         return max(lst)


