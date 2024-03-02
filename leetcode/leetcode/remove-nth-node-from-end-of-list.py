# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        cur=head
        size=0
        while cur:
            size+=1
            cur=cur.next
        if size==1 and n==1:
            return None 
        indx=size-n
        if indx==0:
            temp=head.next
            head=temp
            del temp
            return head
        count=0
        cur=head
        prexev=None
        while cur and cur.next :
            if indx==count+1:
               cur.next=cur.next.next
               break
            else:
                cur=cur.next  
                count+=1
        return head


        