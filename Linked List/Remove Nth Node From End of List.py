# ^^^^^^^^ COPY^^^^^^^^^^^^^
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #brute force method-
        #directly reverse the list and remove the nth node from  front
        dummy=ListNode(0,head) #dummy must be pointing towards head
        right=head
        left=dummy
        
        while n>0 and right:
            right=right.next
            n-=1
        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next #in order to delete nth node of ll
        return dummy.next
            