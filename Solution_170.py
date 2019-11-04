class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.exist = set()
        self.nums = set()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        for num in self.nums:
            self.exist.add(num + number)
        self.nums.add(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        return value in self.exist


        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)