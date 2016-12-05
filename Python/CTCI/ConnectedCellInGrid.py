def get_size_of_field(grid, i, j):
    total_size = 0

    # Check that coord is within bounds.
    if 0 <= j < len(grid) and 0 <= i < len(grid[0]):
        cell_val = grid[j][i]
        grid[j][i] = -1  # Mark as visited.
        if cell_val > 0:
            total_size = 1
            # Left side.
            total_size += get_size_of_field(grid, i - 1, j + 1)
            total_size += get_size_of_field(grid, i - 1, j)
            total_size += get_size_of_field(grid, i - 1, j - 1)
            # Right side.
            total_size += get_size_of_field(grid, i + 1, j - 1)
            total_size += get_size_of_field(grid, i + 1, j)
            total_size += get_size_of_field(grid, i + 1, j + 1)
            # Top and bottom.
            total_size += get_size_of_field(grid, i, j + 1)
            total_size += get_size_of_field(grid, i, j - 1)

    return total_size


def get_biggest_region(grid):
    max_row = len(grid)
    max_col = len(grid[0])
    max_size = -1
    for i in range(max_col):
        for j in range(max_col):
            max_size = max(max_size, get_size_of_field(grid, i, j))

    return max_size

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
