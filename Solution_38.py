class Solution_38:
    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return "1"
        pre = self.countAndSay(n - 1)
        result = []
        i = 0
        while (i < len(pre)):
            Len = 1
            tem = i
            while ((i < len(pre) - 1) and (pre[i] == pre[i + 1])):
                i += 1
                Len += 1
            result.append(str(Len))
            result.append(str(pre[tem]))
            i += 1
        return "".join(result)
