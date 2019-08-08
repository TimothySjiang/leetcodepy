class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        ans = n
        p1 = p2 = -n
        same = word1==word2
        for i in range(n):
            if words[i] == word1:
                p1 = i
                ans = min(ans,p1-p2)
                if same:
                    p2 = p1
            elif not same and words[i] == word2:
                p2 = i
                ans = min(ans,p2-p1)
        return ans