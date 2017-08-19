class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self._empty_grid()

    def toggle_pixel(self, x, y):
        self.grid[y][x] = not self.grid[y][x]

    def _count_neighbors(self, x, y):
        count = 0
        for i, j in (
            (i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)
        ):
            current_x = i + x
            current_y = j + y
            if not (
                0 <= current_x < self.width and
                0 <= current_y < self.width
            ):
                continue
            if self.grid[current_x][current_y]:
                count += 1
        return count

    def step(self):
        new_grid = self._empty_grid()
        for i in range(self.width):
            for j in range(self.height):
                neighbors = self._count_neighbors(i, j)
                if self.grid[i][j]:
                    new_grid[i][j] = (1 < neighbors < 4)
                else:
                    new_grid[i][j] = (neighbors == 3)
        self.grid = new_grid

    def _empty_grid(self):
        return [[False for i in range(self.width)] for j in range(self.height)]

    def print_(self):
        print('\n'.join(
            ''.join(('*' if el else '.') for el in row) for row in self.grid)
        )


if __name__ == '__main__':
    b = Board(8, 8)
    b.toggle_pixel(3, 3)
    b.toggle_pixel(3, 4)
    b.toggle_pixel(3, 5)
    b.print_()
    b.step()
    b.print_()
    b.step()
    b.print_()
