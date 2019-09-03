class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-x for x in nums]
        heapq.heapify(h)
        while k - 1:
            heapq.heappop(h)
            k = k - 1

        return -heapq.heappop(h)