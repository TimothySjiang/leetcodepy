class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        r = [0] * 26
        for c in tasks:
            r[ord(c) - ord('A')] += 1

        r.sort()
        time = 0
        while (r[25] > 0):
            i = 0
            while (i <= n):
                if (r[25] == 0):
                    break
                if (i < 26 and r[25 - i] > 0):
                    r[25 - i] -= 1
                time += 1
                i += 1

            r.sort()

        return time