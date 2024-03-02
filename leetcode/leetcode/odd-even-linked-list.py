# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        ls=[]
        indx=0
        curr=head 
        while curr:
            if indx%2==0:
                ls.append(curr)
            curr=curr.next
            indx+=1
        indx=0
        curr=head
        while curr:
            if indx%2!=0:
                ls.append(curr)
            curr=curr.next
            indx+=1
        
        head = ls[0]
        temp = head
        for i in range(1, len(ls)):
            temp.next = ls[i]
            temp = temp.next
        temp.next = None
        return head

        