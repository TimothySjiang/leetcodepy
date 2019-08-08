class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        table = [collections.defaultdict(int) for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = self.distance(points[i], points[j])
                table[i][distance] += 1
                table[j][distance] += 1

        count = 0
        for i in range(len(points)):
            for dis in table[i]:
                n = table[i][dis]
                count += n * (n - 1)

        return count

    def distance(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2