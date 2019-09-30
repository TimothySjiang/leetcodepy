class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        visited = {}
        newcells = cells
        count = 0
        while tuple(newcells) not in visited and count < N:
            visited[tuple(newcells)] = count
            newcells = self.nextDay(newcells)
            count += 1
        if count == N:
            return newcells
        start = visited[tuple(newcells)]
        circleLength = count - start
        N = (N - start) % circleLength
        for i in range(N):
            newcells = self.nextDay(newcells)
        return newcells

    def nextDay(self, cells):
        newcell = [0] * 8
        for i in range(1, 7):
            newcell[i] = int(cells[i - 1] == cells[i + 1])
        newcell[0] = 0
        newcell[-1] = 0
        return newcell