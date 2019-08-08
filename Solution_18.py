class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            for j in range(l, len(nums) - 2):
                if j > l and nums[j] == nums[j - 1]:
                    continue
                m = j + 1
                r = len(nums) - 1

                while m < r:
                    s = nums[i] + nums[j] + nums[m] + nums[r]
                    if s < target:
                        m += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[m], nums[r]])
                        m += 1
                        r -= 1
                        while m < r and nums[m] == nums[m - 1]:
                            m += 1
                        while m < r and nums[r] == nums[r + 1]:
                            r -= 1

        return res