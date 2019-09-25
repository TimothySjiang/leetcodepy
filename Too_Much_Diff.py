# Given an array A of length N and a number K. For each element A[i] in A you can apply the following operations any number of times:
#
# if A[i] is divisible by K, divide A[i] by K
# if A[i] is not divisible by K, multiply A[i] by K
# Find minimum difference possible between the maximum and minimum number after applying those operations any number of times.
#
# Constraints:
# 1 <= N <= 10,000
# 2 <= K <= 100
#
# Examples:
# A = [87 86 82 49 9] and K = 5 => 42 [Multiply 9 (A[4]) by 5]

from heapq import heappush, heappop
def tooMuchDifference(A, K):
    pq, lb, ub = [], float('inf'), -float('inf')
    for i, x in enumerate(A):
        vals = [x]
        if x % K == 0:
            while x % K == 0:
                x //= K
                vals.append(x)
            vals = vals[::-1]
        else:
            vals.append(x * K)
        lb, ub = min(lb, vals[0]), max(ub, vals[0])
        heappush(pq, vals)
    ans = ub - lb
    while True:
        tup = heappop(pq)
        lb = tup[0]
        ans = min(ans, ub - lb)
        if len(tup) == 1: break
        heappush(pq, tup[1:])
        ub = max(ub, tup[1])
    return ans

print('Q4')
A, K = [87, 86, 82, 49, 9], 5
print(A, K, tooMuchDifference(A, K))
A, K = [90, 20, 18, 17, 9], 5
print(A, K, tooMuchDifference(A, K))
A, K = [125, 25, 24, 26, 4], 5
print(A, K, tooMuchDifference(A, K))
print(' ')