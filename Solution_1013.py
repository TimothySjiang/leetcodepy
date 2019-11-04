class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        target = total//3
        if target * 3 != total:
            return False
        partSum = 0
        count = 0
        for i in range(len(A)):
            partSum += A[i]
            if partSum == target:
                partSum = 0
                count += 1
                if count == 2:
                    return True
        return False