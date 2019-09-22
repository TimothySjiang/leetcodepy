#Long time
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        results = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 and i <= n // i:
                self.recursion(n // i, i, [i], results)
        return results

    def recursion(self, goal, start, result, results):
        results.append(result + [goal])
        for i in range(start, int(goal**0.5)+1):
            if goal % i == 0:
                self.recursion(goal // i, i, result + [i], results)