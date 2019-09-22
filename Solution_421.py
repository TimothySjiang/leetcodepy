#Super
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        Max = 0
        mask = 0
        for i in range(31,-1,-1):
            mask = mask | (1 << i);
            Set = set()
            for num in nums:
                Set.add(num & mask)
            tmp = Max | ( 1 << i)
            for prefix in Set:
                if (tmp ^ prefix) in Set:
                    Max = tmp
                    break
        return Max

