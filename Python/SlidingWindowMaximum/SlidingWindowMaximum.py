from collections import deque


def calc_sliding_window_max(arr, w):
    # Assuming arr is list, and arr > w.
    d = deque()

    # Setup.
    for i in range(w - 1):
        el = arr[i]
        d.append(el)

        while d[0] < el:
            d.popleft()

    # Create B.
    b = []
    for i in range(w - 1, len(arr)):
        el = arr[i]
        d.append(el)
        if len(d) > w:
            d.popleft()

        while d[0] < el:
            d.popleft()
        b.append(d[0])

    return b


if __name__ == '__main__':
    l = [1, 3, -1, -3, 5, 3, 6, 7]
    res = calc_sliding_window_max(l, 3)
    print res
