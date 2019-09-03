class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k,len(nums)):
            if nums[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h,nums[i])
        return h[0]