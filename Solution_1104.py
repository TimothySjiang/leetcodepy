class Solution:
    #????
    def pathInZigZagTree(self, label: int) -> List[int]:
        level, tot = -1, 0
        while label > tot:
            level += 1
            tot += (2 ** level)

        level -= 1
        cur = label // 2
        res = [label]
        while level > -1:
            st, end = 2 ** level, (2 ** (level + 1)) - 1
            cur = st + end - cur
            res.append(cur)
            level -= 1
            cur = cur // 2
        return res[::-1]