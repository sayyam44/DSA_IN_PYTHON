# Definition for singly-linked list.
#https://www.youtube.com/watch?v=G0_I-ZF0S38
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#optimized sol- tc=n,sc=1 (****copy****)
class Solution:
    def reverseList(self, head):
        
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr= nxt
        return prev

#recursive method-tc=n,sc=n
class Solution_rec:
    def rev(self,head):
        if not head:
            return None
        
        newhead=head
        if head.next:
            newhead=self.rev(head.next)
            head.next.next= head
        head.next= None
        return newhead
            

