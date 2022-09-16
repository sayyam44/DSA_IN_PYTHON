# Definition for singly-linked list.
# same as find the duplicate number is list
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #approach 1 - by using hash map
        # iterate through each element and put that node into the hash map and if the same node occurs twice then return 2 i.e. there must be a cycle present
        
        #optimal solution- Tortoise Method 
        #same as find the duplicate number is list 
        #https://leetcode.com/problems/find-the-duplicate-number/
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False