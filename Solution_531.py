class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        dic = collections.defaultdict(list)
        m = len(picture)
        for i in range(m):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    dic[i].append(j)
                    dic[len(picture)+1+j].append(i)
        count = 0
        for i in range(m):
            if len(dic[i]) == 1:
                if len(dic[m + 1 + dic[i][0]]) == 1:
                    count += 1
        return count