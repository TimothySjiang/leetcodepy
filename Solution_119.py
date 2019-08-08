class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res = [0] + res + [0]
            for j in range(len(res)-1):
                res[j] = res[j] + res[j+1]
            res = res[:-1]
        return res