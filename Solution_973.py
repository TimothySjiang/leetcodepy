class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []
        for point in points:
            result.append((point[0]**2+point[1]**2,point))
        result = sorted(result)
        result = [x[1] for x in result]
        return result[:K]