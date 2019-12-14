#TLE
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        queue = [workers[i]+[i] for i in range(len(workers))]
        bikesDict = {}
        for i in range(len(bikes)):
            bikesDict[tuple(bikes[i])] = i
        bikeAssigned = set()
        workerAssigned = set()
        res = [-1] * len(workers)
        visited = set()
        while queue:
            for i in range(len(queue)):
                x, y, w = queue.pop(0)
                if (x,y) in bikesDict and (x,y) not in bikeAssigned and w not in workerAssigned:
                    res[w] = bikesDict[(x,y)]
                    bikeAssigned.add((x,y))
                    workerAssigned.add(w)
                    if len(bikeAssigned) == len(workers):
                        return res
                else:
                    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                        newx, newy = x + dx, y + dy
                        if (newx,newy,w) not in visited:
                            visited.add((newx,newy,w))
                            queue.append((newx,newy,w))