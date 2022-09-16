# https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation
# https://www.youtube.com/watch?v=9VPm6nEbVPA&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=40

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

#tc=n+(n-(n%k))=n,sc=1
# Definition for singly-linked list.
from sklearn.cluster import k_means


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head,k):
        #base condition
        if not head:
            return None
        
        #finding the length of ll
        cur=head
        l=0
        while cur:
            l+=1 #finding the length of ll i.e. l
            cur=cur.next
            
        
        #rationalizing the number of rotations on the given k and length of ll
        if l<k: #if len of ll is smaller than given k 
            rot=k%l
        elif l>k:
            rot=k
        else:
            rot=0
        
        cur.next=head #curr was pointing to last element of ll ,now it will be pointing to head of ll that is iit has become circular ll
        b=head
        steps_from_front=l-rot #since we need to rotate by k times from end #lenght of ll - given k = the node whose pointer need to point at null (i.e. it will be the last element of ll)
        for i in range(steps_from_front-1):
            b=b.next #b has reached the last node of the required ll
        head=b.next #pointing head to the start of new ll
        b.next=None #deleting the connection between lastnode and head node of req ll
        return head
        
            
class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class sol:
    def rot(self,head,k):
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next

        if l>k:
            rot=k
        if l<k:
            rot=k%l
        else:
            rot=0
        
        curr.next=head 
        b=head 
        steps_from_front=l-rot
        for i in range(steps_from_front-1):
            b=b.next
        head=b.next
        head.next=None


