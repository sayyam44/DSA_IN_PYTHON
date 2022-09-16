# 49. Group Anagrams
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

import collections
def groupAnagrams(strs) :
    #using hashmaps tc=m(len of strs)*n(avg len of each string)*26(a-z chars)=m*n
    
    res=collections.defaultdict(list) #res={}
    for s in strs:
        count=[0]*26 # creating an array of 26 0's in which the count will be incremented by one if the chartrer will be present in the string
        for i in s: #iterating through each selected string 
            count[ord(i)-ord("a")]+=1 #incrementing the count of chars in count(with initially 0s) array according to their occurances
                                      #ord function finds the ascii value of a char
        res[tuple(count)].append(s) # creating a hashmap with keys as the char&count of each char in a string and values as the strings with same values(anagrams)
    
    print(res.values()) ##returning only the values that is the grouped anagrams in list
groupAnagrams(["eat","tea","tan","ate","nat","bat"])