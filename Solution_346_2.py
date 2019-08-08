class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.list = []
    def next(self, val: int) -> float:
        if (len(self.list)==self.size):
            del self.list[0]
            self.list.append(val)
            return sum(self.list)/self.size
        else:
            self.list.append(val)
            return sum(self.list)/len(self.list)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)