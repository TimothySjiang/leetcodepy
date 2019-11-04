class Node(object):  # 定义Node类

    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None  # 一个线性表的开头
        self.tail = None  # 一个线性表的结尾
        self.dic = {}  # dic存储信息

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if not self.dic:
            node = Node(key)
            self.dic[key] = node
            self.head = node
            self.tail = node
        else:
            if key not in self.dic:  # 如果不存在，就创建新结点
                node = Node(key)
                self.dic[key] = node
                self.tail.right = node
                node.left = self.tail
                self.tail = node
            else:
                node = self.dic[key]  # +1并且根据count判断是否交换
                node.count += 1
                while node.left and node.count > node.left.count:
                    # swap 2 nodes
                    if self.tail == node:
                        self.tail = node.left
                    self.swap(node.left, node)
                    if not node.left:
                        self.head = node

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.dic:
            return
        else:
            node = self.dic[key]  # 执行-1操作后，并且根据count判断是否进行交换
            node.count -= 1
            while node.right and node.count < node.right.count:
                # swap 2 nodes
                if self.head == node:
                    self.head = node.right
                self.swap(node, node.right)
                if not node.right:
                    self.tail = node

            if not node.count and len(self.dic) == 1:
                self.head = None
                self.tail = None
                self.dic = {}

            if not node.count and node.left:
                self.tail = node.left
                del self.dic[key]
                node.left.right = None

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.head:
            return self.head.key
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.tail:
            return self.tail.key
        else:
            return ""

    def swap(self, left, right):  # 执行结点交换的操作
        leftLeft = left.left
        rightRirhgt = right.right

        left.right = rightRirhgt
        left.left = right
        right.left = leftLeft
        right.right = left
        if rightRirhgt:
            rightRirhgt.left = left
        if leftLeft:
            leftLeft.right = right