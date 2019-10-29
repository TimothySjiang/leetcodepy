class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        nums.append(upper+1)
        pre = lower - 1
        for num in nums:
            if (num == pre + 2):
                result.append(str(num-1))
            elif (num > pre + 2):
                result.append(str(pre + 1) + "->" + str(num -1))
            pre = num
        return result