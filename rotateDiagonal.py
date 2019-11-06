#Quora OA
#First transpose and then left to right
def rotateDiagonal(matrix,k):
    n, k = len(matrix), k%4
    for i in range(k):
        for i in range(n):
            for j in range(i):
                if i != j and i + j != n - 1:
                    matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for i in range(n):
            for j in range(n//2):
                if i != j and i + j != n - 1:
                    matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotateDiagonal(matrix,1)
    print(matrix)
