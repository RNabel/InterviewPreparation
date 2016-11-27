import collections

import sys

Point = collections.namedtuple("Point", ["x", "y"])
memo = {}


def find_minimum_cost_path(start, goal, matrix):
    global memo
    # Handle base case.
    if start == goal:
        return matrix[start.y][start.x]
    elif goal.x < 0 or goal.y < 0:  # If out of bounds.
        return sys.maxint
    elif (start, goal) in memo:
        return memo[(start, goal)]

    # Calculate minimum of paths.
    min_cost = min(
        find_minimum_cost_path(start, Point(goal.x - 1, goal.y), matrix),
        find_minimum_cost_path(start, Point(goal.x - 1, goal.y - 1), matrix),
        find_minimum_cost_path(start, Point(goal.x, goal.y - 1), matrix)
    ) + matrix[goal.y][goal.x]

    memo[(start, goal)] = min_cost  # Remember min cost.
    return min_cost


if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 8, 2],
           [1, 5, 3]]
    cost = find_minimum_cost_path(Point(0, 0), Point(2, 2), mat)
    print cost
