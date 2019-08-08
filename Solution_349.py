class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        l = r = 0
        while l < len(nums1) and r < len(nums2):
            left = nums1[l]
            right = nums2[r]
            if left == right:
                res.append(left)
                while l < len(nums1) and left == nums1[l]:
                    l += 1
                while r < len(nums2) and right == nums2[r]:
                    r += 1
            if right > left:
                while l < len(nums1) and left == nums1[l]:
                    l += 1
            else:
                while r < len(nums2) and right == nums2[r]:
                    r += 1

        return res