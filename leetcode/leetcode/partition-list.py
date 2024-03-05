# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        store=store1=None

        less_x=[]
        greater_x=[]
        cur=head
        while cur:
            if cur.val>=x:
                greater_x.append(cur)
            else:
                less_x.append(cur)
            cur=cur.next
        if len(less_x)>0:
            temp=store=less_x[0]
            for i in range(1,len(less_x)):
                temp.next=less_x[i]
                temp=temp.next
            print(temp.val)
            
        if len(greater_x)>0:
            temp1=store1=greater_x[0]
            for i in range(1,len(greater_x)):
                temp1.next=greater_x[i]
                temp1=temp1.next
            temp1.next=None
        if store:
            if len(greater_x)>0:
                temp.next=greater_x[0]
            return store
        return store1


        