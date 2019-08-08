class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        result = []

        for p in range(len(A)):
            if abs(A[i]) < abs(A[j]):
                result.append(A[j] ** 2)
                j -= 1

            else:
                result.append(A[i] ** 2)
                i += 1

        return result

