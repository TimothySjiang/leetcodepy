class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        table = {}
        if not words:
            return []

        for i, w in enumerate(words):
            table[w] = i

        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                left, right = w[:j], w[j:]
                if left == left[::-1]:
                    rightReverse = right[::-1]
                    if rightReverse in table and table[rightReverse] != i:
                        res.append([table[rightReverse], i])

                if len(right) > 0 and right == right[::-1]:
                    leftReverse = left[::-1]
                    if leftReverse in table and table[leftReverse] != i:
                        res.append([i, table[leftReverse]])

        return res