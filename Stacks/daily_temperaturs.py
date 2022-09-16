# read theory from--https://www.geeksforgeeks.org/count-of-days-remaining-for-the-next-day-with-higher-temperature/
#https://www.youtube.com/watch?v=cTBiBSnjO3c
# https://leetcode.com/problems/daily-temperatures/
#tc=n,sc=n
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#create a stack which will append the temp,its index if the iterated temp value is not greater than the stack's top value
class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        res=[0]*len(tem) #because we need to get 0 vals if we dnt find any greater values 
        # ahead of current val
        stack=[] #pair:[temp,index]
        for i,t in enumerate(tem):
            while stack and t>stack[-1][0]: #iterating till the stack is empty and till the stack's 
                # topmost value is smaller than the t(surrent value)
                stackT,stackI=stack.pop() #storing the temp,index value of the poped value
                #agar traversed temp ki value stack ki top value se badi hui toh stack ki top value k index par 
                #hum res mein jaakar stack k top value index minus traverses temp ka index daal denge 
                res[stackI]=(i-stackI) #now storing the difference in the same index of the poped 
                # value in res
            stack.append([t,i])#if the current t is smaller than the previos vals
        return res
        
        
        
    # brute forse method-- tc=n2, sc=n
        # lst=[]
        # for i in range(len(tem)):
        #     for j in range(i+1,len(tem)):
        #         if tem[j]<=tem[i]:
        #             if j==len(tem)-1 :
        #                 lst.append(0)
        #             else:
        #                 continue
        #         else:
        #             lst.append(j-i)
        #             break
        # lst.append(0)
        # return lst


