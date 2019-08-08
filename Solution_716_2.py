class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        MAX = x if not self.maxStack else self.maxStack[-1]
        self.maxStack.append(MAX if MAX > x else x)
        self.stack.append(x)

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        MAX = self.peekMax()
        buffer = []
        while (self.top() != MAX):
            buffer.append(self.pop())
        self.pop()
        while (buffer):
            self.push(buffer.pop())
        return MAX



        # Your MaxStack object will be instantiated and called as such:
        # obj = MaxStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.peekMax()
        # param_5 = obj.popMax()