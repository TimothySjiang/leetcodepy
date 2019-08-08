class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        self.recursion(s, 0, [], results)
        return results

    def recursion(self, s, pos, result, results):
        if len(result) <= 4:
            if pos == len(s) and len(result) == 4:
                results.append('.'.join(result))
                return
            for i in range(pos, len(s)):
                if s[pos] == '0' and i != pos: break
                m = s[pos:i + 1]
                if int(m) > 255: break
                result += [m]
                self.recursion(s, i + 1, result, results)
                result.pop()


