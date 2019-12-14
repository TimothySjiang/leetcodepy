#MLE
class Solution:
    def confusingNumberII(self, N: int) -> int:
        validMap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        self.count = 0
        val = ''
        for num in validMap:
            if num != '0':
                val += num
                self.backtrack(val, str(N), validMap)
                val = ''
        return self.count

    def backtrack(self, val, N, validMap):
        for i in range(len(val) // 2 + 1):
            if validMap[val[i]] != val[-i - 1]:
                self.count += 1
                break
        for num in validMap:
            if val + num <= N:
                val += num
                self.backtrack(val, N, validMap)
                val = val[:-1]