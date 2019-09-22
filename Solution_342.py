class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if not num : return False
        while not num % 4:
            num /= 4
        return num == 1