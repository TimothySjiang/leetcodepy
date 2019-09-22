class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        results = []
        for i in range(1, n + 1):
            self.recursion(n, k, i + 1, result + [i], results)
        return results

    def recursion(self, n, k, start, result, results):
        if len(result) == k:
            results.append(result)
            return
        for i in range(start, n + 1):
            self.recursion(n, k, i + 1, result + [i], results)