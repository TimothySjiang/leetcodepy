class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = collections.Counter(nums2)
        result = []
        for value in nums1:
            if value in nums2 and c[value] > 0:
                result.append(value)
                c[value] -= 1

        return result