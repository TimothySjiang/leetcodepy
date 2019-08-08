class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left1 = rec1[0:2]
        left2 = rec2[0:2]
        right1 = rec1[2:]
        right2 = rec2[2:]

        if left2[0] < right1[0] and left2[1] < right1[1] and left1[0] < right2[0] and left1[1] < right2[1]:
            return True
        return False