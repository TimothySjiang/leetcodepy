class Solution(object):
    def minIncrementForUnique(self, A):
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) / 2 + give * A[i-1]
                taken -= give

        return int(ans)