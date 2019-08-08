class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size or index < 0:
            return -1
        else:
            p = self.head
            while (index):
                p = p.next
                index -= 1
            return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.newhead = Node(val)
        self.newhead.next = self.head
        self.head = self.newhead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        p = self.head
        if p:
            while (p.next):
                p = p.next
            p.next = Node(val)
            self.size += 1
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.addAtHead(val)

        if index == self.size:
            self.addAtTail(val)
        elif 0 < index < self.size:
            p = Node(val)
            f = self.head
            index -= 1
            while index:
                f = f.next
                index -= 1
            p.next = f.next
            f.next = p

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
        if 0 < index < self.size:
            f = self.head
            index -= 1
            while (index > 0):
                f = f.next
                index -= 1

            if index == self.size - 2:
                f.next = None
            else:
                f.next = f.next.next
            self.size -= 1






            # Your MyLinkedList object will be instantiated and called as such:
            # obj = MyLinkedList()
            # param_1 = obj.get(index)
            # obj.addAtHead(val)
            # obj.addAtTail(val)
            # obj.addAtIndex(index,val)
            # obj.deleteAtIndex(index)