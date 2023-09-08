class Puzzle8:
    def __init__(self, initial_state):
        self.state = initial_state

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.state])

    def get_empty_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def move(self, direction):
        i, j = self.get_empty_position()

        if direction == 'up' and i > 0:
            self.state[i][j], self.state[i - 1][j] = self.state[i - 1][j], self.state[i][j]
        elif direction == 'down' and i < 2:
            self.state[i][j], self.state[i + 1][j] = self.state[i + 1][j], self.state[i][j]
        elif direction == 'left' and j > 0:
            self.state[i][j], self.state[i][j - 1] = self.state[i][j - 1], self.state[i][j]
        elif direction == 'right' and j < 2:
            self.state[i][j], self.state[i][j + 1] = self.state[i][j + 1], self.state[i][j]

    def is_solved(self):
        return self.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial_state = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
puzzle = Puzzle8(initial_state)

while not puzzle.is_solved():
    print(puzzle)
    direction = input("Enter direction (up/down/left/right): ")
    puzzle.move(direction)

print("Congratulations! You solved the puzzle.")
