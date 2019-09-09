class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        visited = set()
        for i in range(len(s)):
            ch = s[i]
            if not res or res[-1] < ch:
                if ch not in visited:
                    res.append(ch)
                    visited.add(ch)
            elif ch not in visited:
                while res and res[-1] in s[i+1:] and res[-1] > ch:
                    visited.discard(res[-1])
                    res.pop()
                res.append(ch)
                visited.add(ch)

        return ''.join(res)