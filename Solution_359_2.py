class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.old = {}
        self.new = {}
        self.timeNew = float('-inf')

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp >= self.timeNew + 20:
            self.old = {}
            self.new = {}
            self.timeNew = timestamp
        elif timestamp >= self.timeNew + 10:
            self.old = self.new
            self.new = {}
            self.timeNew = timestamp

        if message in self.new or (message in self.old and self.old[message] + 10 > timestamp):
            return False
        self.new[message] = timestamp
        return True


        # Your Logger object will be instantiated and called as such:
        # obj = Logger()
        # param_1 = obj.shouldPrintMessage(timestamp,message)