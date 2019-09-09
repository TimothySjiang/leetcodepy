class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        table = {}
        for n in nums2:
            while stack and n > stack[-1]:
                table[stack.pop()] = n
            stack.append(n)
        res = []
        for n in nums1:
            if n in table:
                res.append(table[n])
            else:
                res.append(-1)
        return res