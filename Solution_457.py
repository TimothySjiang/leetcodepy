class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        self.seen = [0] * len(nums)
        for i in range(len(nums)):
            if self.dfs(nums, i):
                return True
        return False

    def dfs(self, nums, i, direction=0):
        if self.seen[i] < 0: return False

        self.seen[i] = 1
        next_i = nums[i] + i
        while next_i < 0:
            next_i += len(nums)
        next_i = next_i % len(nums)
        next_dir = 1 if nums[next_i] > 0 else -1

        if direction and next_dir != direction:
            ans = False
        elif next_i == i:
            ans = False
        elif self.seen[next_i] == 1:
            ans = True
        else:
            ans = self.dfs(nums, next_i, next_dir)
        if not ans: self.seen[i] = -1

        return ans