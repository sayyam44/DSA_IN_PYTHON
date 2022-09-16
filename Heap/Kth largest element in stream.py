# https://www.youtube.com/watch?v=hOjcdrqMoQ8
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
#eg if we have [1,2,2,3] and need to find 3rd largest element then we need to return 2 not 1.

#brute force method is by sorting the given array and then using Binary search in array and find kth largest element
#therefore for searching it will take nlogn time
#similarly for adding we use binary search and check where we can add the element in the sorted array and then add at that point
#this will take n time 

#optimized approach by using MIN HEAP of size K
#tc for add/pop from min heap=n
#tc for getting min value=1

#we would be needing a min heap of size k because in example [4,5,8,2] for finding the 3rd largest element
#we would be never consider 2 for the kth largest value so we will pop 2 
#and then we would be needing the 3rd largest that is the smallest element among the remaining elements
#that will take o(1) time that is why we are using the min heap
#for the constructor func tc=nlog(n)

#for adding an element into min heap directly add the element into the array in 1 time
#then pop the smallest element from the array in log(n) time


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k=nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>k:#if the len of the min heap is greater than the given k then pop from 
            #the min heap that will always pop the min value (0th position)
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val) #add the val into the min heap 
        if len(self.minHeap)>self.k: #we will only popif the len of the min heap is greater than the k
            heapq.heappop(self.minHeap)
        return self.minHeap[0] #min value will always be stored at the 0th index
        
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
