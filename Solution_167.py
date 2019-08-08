class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers)-1
        while(numbers[s]+numbers[e]!=target):
            if numbers[s]+numbers[e] < target:
                s = s + 1
                continue
            if numbers[s] +numbers[e]> target:
                e = e - 1
                continue

        return [s+1,e+1]