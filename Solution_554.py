class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        for row in wall:
            pos = 0
            for i in range(len(row)-1):
                pos += row[i]
                dic[pos] += 1
        return len(wall) - max([dic[x] for x in dic],default=0)