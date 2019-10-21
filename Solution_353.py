class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.snake = collections.deque()
        self.snake.append((0, 0))
        self.snakeSet = set()
        self.snakeSet.add((0, 0))
        self.score = 0
        self.foods = food
        self.foods_index = 0
        self.dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[0]
        dx, dy = self.dir[direction]
        newhead = (head[0] + dx, head[1] + dy)
        if not (0 <= newhead[0] < self.height and 0 <= newhead[1] < self.width):
            return -1
        if self.foods_index < len(self.foods) and newhead == tuple(self.foods[self.foods_index]):
            self.snakeSet.add(newhead)
            self.snake.appendleft(newhead)
            self.foods_index += 1
            self.score += 1
            return self.score
        else:
            self.snakeSet.remove(self.snake.pop())
            if newhead in self.snakeSet:
                return -1
            self.snake.appendleft(newhead)
            self.snakeSet.add(newhead)
            return self.score
        return self.score

        # Your SnakeGame object will be instantiated and called as such:
        # obj = SnakeGame(width, height, food)
        # param_1 = obj.move(direction)