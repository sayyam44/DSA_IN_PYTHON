# https://leetcode.com/problems/contains-duplicate/
# Input: nums = [1,2,3,1]
# Output: true


def containsDuplicate(nums):
    hashset=set()
    for i in nums:
        if i in hashset:
            return True
        else:
            hashset.add(i)
            
#by creating a hashset, tc=o(n),sc=o(n)(for creating hashset)

def containsDuplicate_1st_approach(nums):
    return(any(nums.count(i)>1 for i in nums))
    #time=0(n2),space=o(1)
    
    
def containsDuplicate_my_correct_ans(nums):
    num=list(set(nums))
    return (len(num)!=len(nums))
    