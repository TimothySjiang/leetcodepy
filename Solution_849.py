class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        buff = []
        for i in range(n):
            if seats[i] == 1:
                buff.append(i)

        if len(buff) == 1:
            return max(buff[0], n - 1 - buff[0])

        distance = -float("inf")

        for i in range(len(buff) - 1):
            p1 = buff[i]
            p2 = buff[i + 1]

            distance = max(distance, int((p2 - p1) / 2))

        distance = max(distance, buff[0])
        distance = max(distance, n - 1 - buff[-1])

        return distance
