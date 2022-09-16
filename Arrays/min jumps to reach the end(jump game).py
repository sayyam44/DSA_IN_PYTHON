# https://www.youtube.com/watch?v=muDPTDrpS28
#we will take a parameter reachable initially be 0, now iterate through the array and check the maximum 
#jumps that can happen at that point and if after taking that much of jumps we reach to an index that 
# is greater than the reachable variable then update reachable= i+nums[i] or else reachable will remain 
# same and if at lat reachable is == length of array then yes/True and if the pointer's index while
#  iterating the array is greater than the reachable variable then return False.

class Solution(object):
    def canJump(self, nums):
        n=len(nums)
        reachable=0
        for i in range(n):
            if reachable < i: #here if reachable value is < i index
                return False
            reachable=max(reachable,i+nums[i])
        return True







