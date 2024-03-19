# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        right = head
        while right:
            hold = right.next
            right.next = left
            left = right
            right = hold
            #insertion part
            hold = left
            keeper = None
            while hold.next:
                
                if  hold.next.val < left.val:
                    if hold == left:
                        break
                    keeper = left.next
                    left.next = hold.next
                    hold.next = left
                    break
                
                hold = hold.next
            else:
                if hold != left:
                    keeper = left.next
                    hold.next = left
                    left.next = None
            if keeper:
                left = keeper
        right = left
        left = None
        while right:
            hold = right.next
            right.next = left
            left = right
            right = hold
        return left
        