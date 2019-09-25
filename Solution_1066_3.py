#??
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dis(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        B, W = len(bikes), len(workers)
        dp = [[sys.maxsize] * (1 << B) for _ in range(W + 1)]
        dp[0][0] = 0
        for i, worker in enumerate(workers):
            for bit_bike in range((1 << B)):
                for j, bike in enumerate(bikes):
                    _get, _set = bit_bike & (1 << j), bit_bike | (1 << j)
                    if not _get:
                        dp[i + 1][_set] = min(
                            dp[i + 1][_set],
                            dp[i][bit_bike] + dis(*worker, *bike)
                        )
        return min(dp[-1])