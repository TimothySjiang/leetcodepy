class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        start = 0
        while count < n:
            curr = (start + k) % n
            prev = nums[start]
            while curr != start:
                tmp = nums[curr]
                nums[curr] = prev
                prev = tmp
                curr = (curr + k) % n
                count += 10
            nums[start] = prev
            count += 1
            start += 1
