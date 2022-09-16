# when they ask to return middle of a linked list then we need to return the node which is the middle not the value stored at that node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #tortoise method, tc=n/2,sc=1
        slow=fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
       
        

            
            
            