from heapq import *

class MaxStack:

    def __init__(self):
        self.ls = []        # list (stack)
        self.hp = []        # heap
        self.hpd = set()    # id of items deleted in ls but not hp
        self.lsd = set()    # id of items deleted in hp but not ls
        self.id = 0

    def push(self, x):
        self.ls.append((self.id, x))
        heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self):
        x = self.top()
        self.hpd.add(self.ls[-1][0])
        self.ls.pop()
        return x

    def top(self):
        while self.ls[-1][0] in self.lsd:
            self.lsd.remove(self.ls[-1][0])
            self.ls.pop()
        return self.ls[-1][1]

    def peekMax(self):
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self):
        x = self.peekMax()
        _, nid = heappop(self.hp)
        self.lsd.add(-nid)
        return x

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()