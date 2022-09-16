
def twoSum( nums, target):
    #Hashmap ,tc=n,sc=n
    prev_map={} #value:index, mapping of the prev value from nums
    
    for i,v in enumerate(nums): 
        diff=target-v #finding the diff between the target and the current iterated value and then check whether it  is present in the hashmap or not
        if diff in prev_map:
            return (prev_map[diff],i)
        prev_map[v]=i
        
            


def twoSum_correct_sol(nums,target):
    #tc=n2,space=n
    lst=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                lst.append(i)
                lst.append(j)
                return lst
            else:
                continue