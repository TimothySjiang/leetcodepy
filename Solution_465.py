class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = collections.defaultdict(int)
        for t in transactions:
            m[t[0]] -= t[2]
            m[t[1]] += t[2]
        return self.settle(0, m)

    def settle(self, start, m):
        while start < len(m) and m[start] == 0:
            start += 1
        if start == len(m): return 0
        res = float('inf')
        for i in range(start + 1, len(m)):
            if m[start] * m[i] < 0:
                m[i] = m[start] + m[i]
                res = min(res, 1 + self.settle(start + 1, m))
                m[i] = m[i] - m[start]
        return res