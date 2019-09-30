#Better Understanding
class Node():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)  # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def addNode(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1

    def moveTohead(self, node):
        self.removeNode(node)
        self.addNode(node)

    def popTail(self):
        res = self._sentinel.prev
        self.removeNode(res)
        return res


class LRUCache:
    def __init__(self, capacity: int):
        self._cache = {}
        self.size = 0
        self.capacity = capacity
        self.DLinkedList = DLinkedList()

    def _update(self, node):
        self.DLinkedList.moveTohead(node)

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self._cache:
            newNode = Node(key, value)
            self._cache[key] = newNode
            self.DLinkedList.addNode(newNode)
            self.size += 1
            if self.size > self.capacity:
                node = self.DLinkedList.popTail()
                del self._cache[node.key]
        else:
            node = self._cache[key]
            node.val = value
            self._update(node)


            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)