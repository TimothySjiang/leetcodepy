class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture: return 0
        m, n = len(picture), len(picture[0])
        row = [False] * m
        col = [False] * n
        for i in range(m):
            flag = False
            for j in range(n):
                if picture[i][j] == 'B':
                    if not flag:
                        flag = True
                    else:
                        flag = False
                        break
            if flag:
                row[i] = True

        for j in range(n):
            flag = False
            for i in range(m):
                if picture[i][j] == 'B':
                    if not flag:
                        flag = True
                    else:
                        flag = False
                        break
            if flag:
                col[j] = True
        count = 0
        for i in range(m):
            for j in range(n):
                if row[i] and col[j] and picture[i][j] == 'B':
                    count += 1
        return count

