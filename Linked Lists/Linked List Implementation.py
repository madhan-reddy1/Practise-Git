class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1 

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        
        else:
            self.head = node
            self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        i = 0
        while cur:
            if i == index-1:
                node = Node(val)
                nextnode = cur.next
                cur.next = node
                node.next = nextnode
                if not nextnode:
                    self.tail = node
                return
            cur = cur.next
            i += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                if self.head == self.tail:
                    self.tail = self.tail.next
                self.head = self.head.next
            return

        cur = self.head
        i = 0
        while cur:
            if i == index-1:
                if cur.next:
                    cur.next = cur.next.next
                    if not cur.next:
                        self.tail = cur
                return
            cur = cur.next
            i += 1
        return
    