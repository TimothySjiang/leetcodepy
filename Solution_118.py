class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        i = 0
        while i < numRows:
            buff = []
            if i > 0:
                buff2 = [0] + result[-1] + [0]
                for i in range(len(buff2) - 1):
                    buff.append(buff2[i] + buff2[i + 1])
                result.append(buff)

            else:
                result.append([1])

            i = i + 1

        return result