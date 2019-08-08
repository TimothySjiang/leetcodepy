class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A) - 1

        if len(A) == 1:
            return A[0]

        while l <= r:
            mid = l + (r - l) // 2

            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            else:
                if A[mid - 1] < A[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

