#TLE
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        h = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dis = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                h.append((dis, i, j))
        heapq.heapify(h)
        assignedWorker = set()
        assignedBike = set()
        res = [-1] * len(workers)
        while len(assignedWorker) != len(workers):
            _, worker, bike = heapq.heappop(h)
            if worker not in assignedWorker and bike not in assignedBike:
                res[worker] = bike
                assignedWorker.add(worker)
                assignedBike.add(bike)
        return res

