# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution:
    def countCharacters(self, words ,chars):
        ans=0
        for word in words:
            flag=1
            for char in word:
                if chars.count(char)<word.count(char): #if count of each character in a word is greater than the count of that same char in chars 
                    flag=0
                    break
            if flag==1:
                ans+=len(word)
        return ans
                
