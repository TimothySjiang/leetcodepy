class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        return [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])