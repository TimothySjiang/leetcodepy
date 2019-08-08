class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        n = len(candies)
        brother = n / 2

        table = collections.defaultdict(int)
        for c in candies:
            table[c] += 1

        kind = len(table)

        for c in table:
            if table[c] >= 2:
                brother -= table[c] - 1

        brother = max(0, brother)

        return int(kind - brother)

