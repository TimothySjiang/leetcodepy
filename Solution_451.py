class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ''
        table = collections.defaultdict(int)
        for w in s:
            table[w] += 1

        h = []
        for w in table:
            heapq.heappush(h, (-table[w], w))

        res = ''
        while h:
            w = heapq.heappop(h)
            res += w[1] * (-w[0])

        return res