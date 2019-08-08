class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = float("inf")
        min2 = float("inf")
        max1 = -float("inf")
        max2 = -float("inf")
        max3 = -float("inf")
        for value in nums:
            if value < min1:
                min2 = min1
                min1 = value

            elif value < min2:
                min2 = value

            if value > max1:
                max3 = max2
                max2 = max1
                max1 = value
            elif value > max2:
                max3 = max2
                max2 = value
            elif value > max3:
                max3 = value

        return max(min1 * min2 * max1, max1 * max2 * max3)