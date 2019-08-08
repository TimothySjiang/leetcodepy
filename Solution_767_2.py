class Solution:
    def reorganizeString(self, S: str) -> str:
        N = len(S)
        A = []
        for c,x in sorted((S.count(x),x) for x in set(S)):
            if c > (N+1)/2: return ""
            A+=[x]*c
        ans = [None]*N
        ans[::2],ans[1::2] = A[N//2:],A[:N//2]
        return "".join(ans)