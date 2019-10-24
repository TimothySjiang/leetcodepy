class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        for i in range(len(values) - 1, -1, -1):
            if timestamp >= values[i][0]:
                return values[i][1]
        return ''


        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)