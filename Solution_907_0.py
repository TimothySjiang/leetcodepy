class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        if not A: return 0
        total = 0
        for i in range(len(A)):
            for j in range(i+1,len(A)+1):
                total += min(A[i:j])
        return total