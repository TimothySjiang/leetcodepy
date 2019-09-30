#TLE
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        for i in range(N):
            newcells = [0]*8
            for i in range(1,7):
                newcells[i] = int(cells[i-1] == cells[i+1])
            cells = newcells
        return cells