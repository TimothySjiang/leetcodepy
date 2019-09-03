class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if self.minh and self.minh[0] < num:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -num)

        if len(self.maxh) == len(self.minh) + 2:
            heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        elif len(self.maxh) == len(self.minh) - 2:
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))

    def findMedian(self) -> float:
        if len(self.maxh) < len(self.minh):
            return self.minh[0]
        elif len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        return (-self.maxh[0] + self.minh[0]) / 2

        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()