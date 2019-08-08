class Solution:
    def fourSumCount(self, A, B, C, D):
        map = collections.defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                sum = A[i] + B[j]
                map[sum] += 1

        for i in range(len(C)):
            for j in range(len(D)):
                sum = -(C[i] + D[j])
                if sum in map:
                    ans += map[sum]
        return ans