# https://leetcode.com/problems/count-binary-substrings/
# https://leetcode.com/problems/count-binary-substrings/discuss/1172569/Short-and-Easy-w-Explanation-and-Comments-or-Keeping-Consecutive-0s-and-1s-Count-or-Beats-100
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans,prev,curr=0,0,1
        for i in range(len(s)):
            if s[i]!=s[i-1]:
                ans+=min(prev,curr) #binary substrins will always be the min of the 2 continoust
                # substrings of 0's and 1's eg for 0000111 ans=3
                prev=curr
                curr=1
            else:
                curr+=1
        ans+=min(prev,curr) #this is if i reaches the len(s) 
        return ans
