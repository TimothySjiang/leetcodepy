class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if (image[sr][sc] == newColor):
            return image

        def adjacent_flood(sr, sc):
            adjacent = (sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)
            for x, y in adjacent:
                if (x >= 0) and (x < len(image)) and (y >= 0) and (y < len(image[0])) and (image[x][y] == color):
                    image[x][y] = newColor
                    adjacent_flood(x, y)

        color = image[sr][sc]
        image[sr][sc] = newColor

        adjacent_flood(sr, sc)

        return image