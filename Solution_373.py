class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 : return []
        h = [(nums1[0]+nums2[0],0,0)]
        pairs = []
        while h and len(pairs) < k:
            _, i, j = heapq.heappop(h)
            pairs.append([nums1[i], nums2[j]])
            if i < len(nums1) and j+1 < len(nums2):
                heapq.heappush(h, [nums1[i] + nums2[j+1], i, j+1])
            if i+1 < len(nums1) and j == 0:
                heapq.heappush(h, [nums1[i+1] + nums2[0], i+1, 0])
        return pairs