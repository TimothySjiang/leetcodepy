
def strokesRequired(picture):
    # Write your code here
    count = 0
    m = len(picture)
    n = len(picture[0])
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i,j) not in visited:
                color = picture[i][j]
                dfs(picture,i,j,color,visited)
                count += 1
    return count

def dfs(picture,i,j,color,visited):
    if not (0 <= i < len(picture) and 0 <= j < len(picture[0]) and picture[i][j] == color and (i,j) not in visited):
        return
    visited.add((i,j))
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        newx = i + dx
        newy = j + dy
        dfs(picture,newx,newy,color,visited)

if __name__ == '__main__':
    strokesRequired()