#implement queue with limited size of arrays
class Node:
    def __init__(self):
        self.next = None

class queue:
    def __init__(self):
        self.first= [None] * 10
        self.last = self.first
        self.start = 0
        self.end = 0

    def add(self,n):
        self.last[self.end] = n
        self.end += 1
        if self.end == 9:
            self.last[9] = Node()
            self.last[9].next = [None] * 10
            self.last = self.last[9].next
            self.end = 0

    def pop(self):
        res = self.first[self.start]
        self.start += 1
        if self.start == 9:
            self.first = self.first[9].next
            self.start = 0
        return res

