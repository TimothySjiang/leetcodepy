class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack =  []
        self.minstack = []

    def push(self, x: int) -> None:
        self.minstack.append(x if not self.minstack else min(x,self.minstack[-1]))
        self.stack.append(x)

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        MIN = self.minstack[-1]
        return MIN


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()