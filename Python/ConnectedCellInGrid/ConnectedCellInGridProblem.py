import sys


def parse_grid(string):
    string = string.strip()
    lines = string.split('\n')
    rows = int(lines[0])
    columns = int(lines[1])
    grid = []

    for line in lines[2:]:
        grid.append([int(x) for x in line.split(' ')])

    return grid


def floodfill(grid, x, y, max_row, max_col):
    total = 0
    cell_value = grid[y][x]  # Column major order.

    if cell_value > 0:
        total = 1
        grid[y][x] = -1  # Set to visited.

        # Directly next to each other.
        if x > 0:
            total += floodfill(grid, x - 1, y, max_row, max_col)
        if x < max_col:
            total += floodfill(grid, x + 1, y, max_row, max_col)
        if y > 0:
            total += floodfill(grid, x, y - 1, max_row, max_col)
        if y < max_row:
            total += floodfill(grid, x, y + 1, max_row, max_col)
        # Diagonal fields.
        if x > 0 and y > 0:  # Top left.
            total += floodfill(grid, x - 1, y - 1, max_row, max_col)
        if x < max_col and y > 0:  # Top right.
            total += floodfill(grid, x + 1, y - 1, max_row, max_col)
        if x < max_col and y < max_row:  # Bottom right
            total += floodfill(grid, x + 1, y + 1, max_row, max_col)
        if x > 0 and y < max_row:  # Bottom right
            total += floodfill(grid, x - 1, y + 1, max_row, max_col)

    return total


if __name__ == '__main__':
    rows = int(sys.stdin.readline())
    cols = int(sys.stdin.readline())
    grid = "%d\n%d\n" % (rows, cols)
    for i in range(rows):
        grid += sys.stdin.readline().strip("\r")
    parsed_grid = parse_grid(grid)
    max_count = 0

    for i in range(cols):
        for j in range(rows):
            count = floodfill(parsed_grid, i, j, rows - 1, cols - 1)
            max_count = max(max_count, count)

    print max_count
