class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # Write your code here
        c = [0 for i in range(0, 200)]
        for i in range(0, len(hand)):
            c[ord(hand[i])] += 1
        return self.aux(board, c)

    def aux(self, s, c):
        if s == "":
            return 0
        res = 2 * len(s) + 1
        i = 0
        while i < len(s):
            j = i  # j保存起点
            i += 1
            while i < len(s) and s[i] == s[j]:
                i += 1
            inc = 3 - i + j  # 3-(i-j) 判断消除需要几个球
            if c[ord(s[j])] >= inc:  # 如果数量足够
                used = 0 if inc <= 0 else inc  # 如果inc<=0，不需要
                c[ord(s[j])] -= used  # 用掉s[j]
                temp = self.aux(s[0: j] + s[i:], c)  # 去除j至i的一段继续搜索
                if temp >= 0:
                    res = min(res, used + temp);
                c[ord(s[j])] += used  # 搜索完成后补充球的数量
        return -1 if res == 2 * len(s) + 1 else res