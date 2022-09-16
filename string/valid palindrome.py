# https://leetcode.com/problems/valid-palindrome/
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_out=''
        for char in s:
            if char.isalnum():
                s_out += char.lower()
        return s_out==s_out[::-1]
        