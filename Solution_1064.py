class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        l = 0
        r = len(A) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if A[mid] == mid:
                return mid
            else:
                if A[mid] < mid:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1