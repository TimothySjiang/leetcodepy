# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 0
        length = mountain_arr.length()
        right = length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid
            else:
                left = mid + 1

        pivot = left
        right = pivot
        left = 0
        while left < right:
            mid = left + (right - left) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                right = mid
            else:
                left = mid + 1

        left = pivot
        right = mountain_arr.length()
        while left < right:
            mid = left + (right - left) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num < target:
                right = mid
            else:
                left = mid + 1
        return -1
