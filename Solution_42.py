class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = []
        leftmax = 0
        for h in height:
            leftmax = max(leftmax, h)
            left.append(leftmax)

        right = []
        rightmax = 0
        for h in height[::-1]:
            rightmax = max(rightmax, h)
            right.append(rightmax)
        right = right[::-1]

        result = 0
        for i, h in enumerate(height):
            result += min(left[i], right[i]) - h

        return result