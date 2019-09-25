class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        dic = {}

        def helper(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def dfs(p, arr):
            if p == len(workers):
                return 0
            if (p, tuple(arr)) in dic:
                return dic[(p, tuple(arr))]
            temp = float('inf')
            for i in range(len(arr)):
                if arr[i] == 0:
                    temp = min(temp, helper(bikes[i], workers[p]) + dfs(p + 1, arr[:i] + [1] + arr[i + 1:]))
            dic[(p, tuple(arr))] = temp
            return temp

        ans = dfs(0, [0 for _ in range(len(bikes))])
        return ans