#Quora OA
def diagonalSort(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for d in range(n):
        temp = sorted([matrix[i][i+d] for i in range(n-d)])
        for i in range(n-d):
            matrix[i][i+d] = temp[i]
        if d:
            temp = sorted([matrix[i + d][i] for i in range(n-d)])
            for i in range(n-d):
                matrix[i+d][i] = temp[i]

if __name__ == '__main__':
    matrix = [[8,4,1],[4,4,1],[4,8,9]]
    diagonalSort(matrix)
    print(matrix)