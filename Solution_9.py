class Solution():
    def isPalindrome(self, x):
        result = 0
        old = x
        while (x != 0):
            tail = x % 10
            newResult = result * 10 + tail
            if ((newResult - tail) / 10 != result):
                return False
            result = newResult
            x = x // 10

        return result == old

