class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f - i + 1
            ans += [i, N]
            N -= 1
        return ans