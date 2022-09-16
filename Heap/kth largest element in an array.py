# https://leetcode.com/problems/kth-largest-element-in-an-array/
# https://www.youtube.com/watch?v=XEmy13g1Qxc
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

#brute force by using sorting (tc=nlogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]


#Optimized approach- n (for converting array into heap) + klogn(logn for poping from the heap and we need to pop k times)

#most optimized approach tc=o(n) avg case , o(n2) worst case
#QUICK SORT 
#eg - given 3,2,1,5,6,4 leats say 4 is pivot point 
#then start from 3 and go upto pivot point 
#if the ith value is smaller then the pivot point then put the ith value in the 1st half 
#but not necessarily in sorted orde
#3,2,1,4(p),6,5
#now if we want 3rd larget value then 4 will be the output directly as 4 is the pivot point
#but other thrn 4 if we want 4th largest then go to 4th value that is 6 and repeat the process
#that turns it into 3,2,1,4(p),5,6 return 5 as required

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #eg given ---- 3,2,1,5,6,4
        nums.sort()
        return nums[len(nums) - k]

        k = len(nums) - k

        def quickSelect(l, r):
            if l == r:
                return nums[l]

            pivot, p = nums[r], l#pivot is the rightmost value and p is the leftmost value
            for i in range(l, r):
                if nums[i] <= pivot: #and if it is greater then dont move p pinter and dont put any value
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1    #p pointer is moved by 1 everytime that is to an empty space
            #here we will reach to a point p which tells that every element before p pointer is <= poiner value and towards p's right is greater than pointer value 
            # 3,2,1,5(p),6,4(r)
            nums[p], nums[r] = nums[r], nums[p]
            #3,2,1,4(p),6,5

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                # this case will run as p=4,k=6
                #so again run quickselect for 6(p),5
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
                
        
