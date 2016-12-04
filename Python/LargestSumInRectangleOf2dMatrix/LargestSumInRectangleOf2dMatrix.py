import sys
# Memo for DP algorithm.
max_sums = {}


def find_largest(arr, i, j, size, rows, cols):
    # Handle base cases.
    if size == 1:  # If size == 1 just return value of cell.
        if i < cols and j < rows:
            return arr[j][i]
        else:  # Value is out of bounds - return a really small number.
            return -(sys.maxint - 1)

    else:
        # Check if grid of specified size was already calculated.
        if (i, j, size) in max_sums:
            return max_sums[(i, j, size)]

        # Calculate sum of current grid.
        current_sum = 0
        for x in range(i, i + size):
            for y in range(j, j + size):
                current_sum += arr[y][x]

        # Get maximum sum from current grid and all possible sub grids.
        current_best = max(
            current_sum,
            find_largest(arr, i, j, size - 1, rows, cols),
            find_largest(arr, i + 1, j, size - 1, rows, cols),
            find_largest(arr, i + 1, j + 1, size - 1, rows, cols),
            find_largest(arr, i, j + 1, size - 1, rows, cols)
        )

        # Memoize max cost of current grid.
        max_sums[(i, j, size)] = current_best

        return current_best


if __name__ == '__main__':
    arr = [[1, 2, -1, -4, -20],
           [-8, -3, 4, 2, 1],
           [3, 8, 10, 1, 3],
           [-4, -1, 1, 7, -6]]

    maximum = find_largest(arr, 0, 0, len(arr), len(arr), len(arr[0]))
    print maximum
