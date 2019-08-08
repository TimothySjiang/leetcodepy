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
            table.setdefault(n, -1)
            res.append(table[n])

        return res
