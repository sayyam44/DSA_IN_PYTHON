# ^^^^^^^^^^^^^^^COPY^^^^^^^^^^^^^^^^^^^
# https://leetcode.com/problems/sliding-window-maximum/
# https://leetcode.com/problems/sliding-window-maximum/discuss/237611/Simplest-O(n)-Python-Solution-with-Explanation
# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []
        for i, n in enumerate(nums): 
            while d and nums[d[-1]] < n: #nums[d[-1]] means the topmost element in dequeue from back 
                d.pop()
            d.append(i)
            if d[0] == i - k: #window out of range case here d[0] means the topmost element from fron in deque
                d.popleft()
            if i>=k-1:
                out.append(nums[d[0]]) #as the elements are always stored in decreasing format in deque
                #so the elemets at the top of deque will alwys be the largest value 
        return out

#EXAMPLE
# i = 0, curr element = 8, d = deque([]) and out = []
# 	 Added i to d
# i = 1, curr element = 3, d = deque([0]) and out = []
# 	 Added i to d
# i = 2, curr element = -1, d = deque([0, 1]) and out = []
# 	 Added i to d
# 	 Append nums[d[0]] = 8 to out
# i = 3, curr element = -3, d = deque([0, 1, 2]) and out = [8]
# 	 Added i to d
# 	 Popped left from d because it's outside the window's leftmost (i-k)
# 	 Append nums[d[0]] = 3 to out
# i = 4, curr element = 5, d = deque([1, 2, 3]) and out = [8, 3]
# 	 Popped from d because d has elements and nums[d.top] < curr element
# 	 Popped from d because d has elements and nums[d.top] < curr element
# 	 Popped from d because d has elements and nums[d.top] < curr element
# 	 Added i to d
# 	 Append nums[d[0]] = 5 to out
# i = 5, curr element = 3, d = deque([4]) and out = [8, 3, 5]
# 	 Added i to d
# 	 Append nums[d[0]] = 5 to out
# i = 6, curr element = 6, d = deque([4, 5]) and out = [8, 3, 5, 5]
# 	 Popped from d because d has elements and nums[d.top] < curr element
# 	 Popped from d because d has elements and nums[d.top] < curr element
# 	 Added i to d
# 	 Append nums[d[0]] = 6 to out
# i = 7, curr element = 7, d = deque([6]) and out = [8, 3, 5, 5, 6]
# 	 Popped from d because d has elements and nums[d.top] < curr element
# 	 Added i to d
# 	 Append nums[d[0]] = 7 to out
# [8, 3, 5, 5, 6, 7]