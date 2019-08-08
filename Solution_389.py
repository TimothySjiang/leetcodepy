class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table = collections.defaultdict(int)
        for w in s:
            table[w] += 1

        for w in t:
            table[w] -= 1

        for w in table:
            if table[w] < 0:
                return w

