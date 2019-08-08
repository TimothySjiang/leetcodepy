class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {}
        for i,c in enumerate(S):
            d[c] = i
        anchor =  j = 0
        ans = []
        for i,c in enumerate(S):
            j = max(j,d[c])
            if i == j:
                ans.append(i-anchor+1)
                anchor = i + 1
        return ans