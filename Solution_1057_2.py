class Solution:
    def assignBikes(self, workers, bikes):
        distances = collections.defaultdict(list)
        for i,worker in enumerate(workers):
            for j,bike in enumerate(bikes):
                dis = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances[i].append((dis, i, j))
            distances[i].sort(reverse = True)
        h = [distances[i].pop() for i in distances]
        heapq.heapify(h)
        assignedBike = set()
        res = [-1] * len(workers)
        while len(assignedBike) != len(workers):
            _, worker, bike = heapq.heappop(h)
            if bike not in assignedBike:
                res[worker] = bike
                assignedBike.add(bike)
            else:
                heapq.heappush(h, distances[worker].pop())
        return res