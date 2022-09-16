
# https://leetcode.com/problems/top-k-frequent-elements/
# https://www.youtube.com/watch?v=YPTqKIgVk-k
#Input: nums = [1,1,1,2,2,3,3,4], k = 3
# Output: [1,2,3]

#tc=n+n+n(for 3 for loops)=n,sc=n
def topKFrequent(nums,k):
    count={} # creating hashmap to count the occurances of each value
    freq=[[] for i in range (len(nums)+1)] 
    #creating an array freq of same size of input array , index:= count/freq of the element, value=list of the numbers that occured that number of time
    for n in nums:
        # +countS.get(s[i],0) this gives the previous value(no. of counts)
        count[n]=1+count.get(n,0) #iterating through each element in nums and counting how many times it occured
        #get(n,0) means if n doesnt exists then count = 0
        #count={1: 3, 2: 2, 3: 2, 4: 1}
    for n,c in count.items(): #n=value,c=n's frequency
        freq[c].append(n) #this shows the number n occured c number of times, index=count ,value=list of all numbers that occured c number of times (already in ascending order)
        #freq=[[], [4], [2, 3], [1], [], [], [], [], []]
    res=[]
    for i in range(len(freq)-1,0,-1): #iterating in ascending order of the frequency e.g. 6,5,4,3,2,1,0 because we want the 1st k elementsthat is bigges count's values first
        for n in freq[i]: #for iterating throu each element for the list present in each index 
            res.append(n)
            if len(res)==k:
                return res
