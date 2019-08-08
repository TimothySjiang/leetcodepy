class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        n = len(s)
        targetHash = collections.Counter(t)
        UniqueChar = len(targetHash)

        MatchedChar = 0
        window = collections.defaultdict(int)

        minLength = n + 1
        res = ''
        j = 0
        for i in range(n):
            while j < n and MatchedChar < UniqueChar:
                if s[j] in targetHash:
                    window[s[j]] += 1

                    if window[s[j]] == targetHash[s[j]]:
                        MatchedChar += 1
                j += 1

            if j - i < minLength and MatchedChar == UniqueChar:
                minLength = j - i
                res = s[i:j]

            if s[i] in targetHash:
                if window[s[i]] == targetHash[s[i]]:
                    MatchedChar -= 1
            window[s[i]] -= 1

        return res