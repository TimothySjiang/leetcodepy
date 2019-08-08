class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            j = i
            while True:
                if j + 1 < len(nums) and nums[j] + 1 == nums[j + 1]:
                    j += 1
                    continue
                else:
                    if j == i:
                        res.append(str(nums[i]))
                        break
                    else:
                        res.append(str(nums[i]) + "->" + str(nums[j]))
                        break
            i = j + 1

        return res
