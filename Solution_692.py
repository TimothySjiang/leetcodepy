class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        table = collections.Counter()
        for w in words:
            table[w] += 1

        h = []
        for w in table:
            heapq.heappush(h, (-table[w], w))
        res = []
        while k:
            res.append(heapq.heappop(h)[1])
            k -= 1

        return res
