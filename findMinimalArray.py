import collections
def minimalArray(m,n,queries):
    map = collections.defaultdict(int)
    matrix = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = (i + 1) * (j + 1)
            map[matrix[i][j]] += 1

    res = []
    candidates = sorted(map)
    startIndex = 0
    for query in queries:
        if len(query) == 1:
            for index in range(startIndex,len(candidates)):
                val = candidates[index]
                if map[val]:
                    res.append(val)
                    startIndex = index
                    break
        elif len(query) == 2:
            if query[0] == 1:
                row = query[1]
                for j in range(n):
                    if matrix[row][j] != -1:
                        map[matrix[row][j]] -= 1
                        matrix[row][j] = - 1
            else:
                col = query[1]
                for i in range(m):
                    if matrix[i][col] != -1:
                        map[matrix[i][col]] -= 1
                        matrix[i][col] = - 1

    return res

if __name__ == '__main__':
    print(minimalArray(3,3,[[1],[1,2],[2,0],[1,0],[1]]))


