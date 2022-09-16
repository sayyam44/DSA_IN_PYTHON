# https://www.youtube.com/watch?v=_vzVGhKt70o
# https://leetcode.com/problems/count-and-say/

# Input: n = 4
# Output: "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        
        prev=self.countAndSay(n-1)
        res=""
        ct=1

        for i in range(len(prev)):
            if i==len(prev)-1 or prev[i]!=prev[i+1]: #if i is at the last element of previous or i and i+1 are not equal in previous 
                res+=str(ct)+prev[i]
                ct=1
            else:
                ct+=1
        return res
