class Vector2D:
    def __init__(self, vec2d):
        self.col = 0
        self.row = 0
        self.vec = vec2d

    # @return {integer}
    def next(self):
        if self.hasNext():
            result = self.vec[self.row][self.col]
            self.col += 1
            return result

    def hasNext(self):
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True

            self.col = 0
            self.row += 1

        return False

        # Your Vector2D object will be instantiated and called as such:
        # obj = Vector2D(v)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()