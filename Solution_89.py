class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        size = 1 << n
        for i in range(size):
            ans.append((i >> 1) ^ i)
        return ans