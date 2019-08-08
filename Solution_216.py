class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.limit = k
        self.dfs(target=n, index=1, path=[])
        return self.res

    def dfs(self, target, index, path):
        if target == 0 and self.limit == len(path):
            self.res.append(path)
        if self.limit == len(path):
            return
        for i in range(index, 10):
            if target - i < 0:
                break
            self.dfs(target - i, i + 1, path + [i])
