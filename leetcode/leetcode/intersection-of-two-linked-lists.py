# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==headB:
            return headA
        lsA=[]
        lsB=[]
        cur1=headA
        cur2=headB
        while cur1:
            lsA.append(cur1)
            cur1=cur1.next
        while cur2:
            lsB.append(cur2)
            cur2=cur2.next
        lenn=0
        if len(lsA)<len(lsB):
            lenn=len(lsA)
        else:
            lenn=len(lsB)
        j=len(lsA)-1
        k=len(lsB)-1
        for i in range(lenn-1,-1,-1):
            if i==lenn-1 and (lsA[j]!=lsB[k]):
                return None
            if i!=lenn-1 and (lsA[j]!=lsB[k]):
                return lsA[j+1]
            j-=1
            k-=1
        return lsA[j+1]
        
            

        