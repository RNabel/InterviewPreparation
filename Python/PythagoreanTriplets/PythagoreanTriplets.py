def find_pair(arr, i):
    c = arr[i]
    subset = arr[:i]
    # DP memo.
    element_map = {}

    for i, x in reversed(list(enumerate(subset))):
        el = arr[i]

        if c - el in element_map:
            return el, c - el
        else:
            element_map[el] = True

    return False


def find_squares(arr):
    arr = [x ** 2 for x in arr]
    arr.sort()

    for i, c in reversed(list(enumerate(arr))):  # Fix c in decreasing order.
        # Find (a, b) such that a + b = c.
        pair = find_pair(arr, i)
        if pair:
            return c, pair[0], pair[1]

    return False


if __name__ == '__main__':
    arrYes = [3, 1, 4, 6, 5]
    arrNo = [10, 4, 6, 12, 5]

    print find_squares(arrYes)
    print find_squares(arrNo)
