#Show OFF!
class BITree():
    def __init__(self, size):
        self.tree = [0] * size
        self.size = size

    def update(self, i, k):
        while i < self.size:
            self.tree[i] += k
            i += (i & -i)

    def getSum(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= (i & -i)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        bitTree = BITree(N + 1)

        for x in reversed(nums):
            res.append(bitTree.getSum(rank[x] - 1))
            bitTree.update(rank[x], 1)
        return res[::-1]