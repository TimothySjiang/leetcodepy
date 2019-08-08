class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = {}
        for i, val in enumerate(nums):
            if val not in result.keys():
                result[val] = i
            else:
                if i - result[val] <= k:
                    return True
                else:
                    result[val] = i

        return False
