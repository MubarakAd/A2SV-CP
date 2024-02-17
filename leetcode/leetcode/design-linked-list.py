

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  

class MyLinkedList:

    def __init__(self, val=0, next=None):
        self.head=None
        

    def get(self, index: int) -> int:
        temp=self.head
        for i in range(index):
            if temp:
                temp=temp.next
        if temp:
            return temp.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node=Node(val,self.head)
        self.head=node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=Node(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.head=Node(val,self.head)
        else:
            temp=self.head
            for _ in range(index-1):
                if temp:
                    temp=temp.next
            if temp:
                node=Node(val,temp.next)
                temp.next=node
        
    def deleteAtIndex(self, index: int) -> None:
        if self.head and index==0:
            self.head=self.head.next
        else:
            temp=self.head
            for _ in range(index-1):
                if temp:
                    temp=temp.next
            if temp and temp.next:
                temp.next=temp.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
