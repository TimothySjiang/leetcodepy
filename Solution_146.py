class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None


class LRUCache:
    def _popTail(self):
        res = self.tail.prev
        self._removeNode(res)
        return res

    def _removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def _addNode(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

        if self.size > self.capacity:
            tail = self._popTail()
            del self.cache[tail.key]

    def _moveTohead(self, node):
        self._removeNode(node)
        self._addNode(node)

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.size = 0
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._moveTohead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            newnode = DLinkedNode()
            newnode.key = key
            newnode.val = value
            self.cache[key] = newnode
            self._addNode(newnode)
        else:
            node.val = value
            self._moveTohead(node)





            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)