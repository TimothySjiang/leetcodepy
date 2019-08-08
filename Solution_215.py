class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums:
            heapq.heappush(h, -x)

        while k - 1:
            heapq.heappop(h)
            k = k - 1

        return -heapq.heappop(h)