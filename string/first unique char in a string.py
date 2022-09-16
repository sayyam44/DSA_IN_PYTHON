# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
                
        index=-1
        for i in range(len(s)):
            if h[s[i]]==1:
                index=i
                break
        return index