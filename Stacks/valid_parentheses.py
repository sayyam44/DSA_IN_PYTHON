#^^^^^COPY^^^^^^
# https://leetcode.com/problems/valid-parentheses/
# Input: s = "()[]{}"
# Output: true
#tc=n,sc=n
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={")":"(","]":"[","}":"{"} #keys are closing and vals are opening brackets
        
        for c in s:
            if c not in closetoopen: #if c is not any closing bracket
                stack.append(c)
                continue
            if not stack or stack[-1]!=closetoopen[c]: #the corresponding value of c in close to open must be same as stack's top value
                return 0
            stack.pop()
        return not stack #RETURN TRUE IF STACK IS EMPTY

