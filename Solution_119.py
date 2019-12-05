class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        new = [1]
        last = [0] + new + [0]
        for i in range(rowIndex):
            new = []
            for j in range(len(last) - 1):
                new.append(last[j] + last[j + 1])
            last = [0] + new + [0]
        return new
