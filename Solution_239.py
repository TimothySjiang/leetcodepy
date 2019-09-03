class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums : return nums
        deque = []
        res = []
        for i in range(len(nums)):
            if deque and deque[0] == i-k:
                deque.pop(0)
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i+1 >= k:
                res.append(nums[deque[0]])
        return res