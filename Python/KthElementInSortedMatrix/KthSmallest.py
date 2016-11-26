import sys
import collections
import heapq

HEntry = collections.namedtuple("HEntry", ["val", "x", "y"])


def findKthSmallest(mat, rows, cols, k):
    # Populate the heap.
    heap = [HEntry(mat[0][i], i, 0) for i in range(cols)]
    heapq.heapify(heap)

    for i in range(k-1):
        # Retrieve element.
        el = heapq.heappop(heap)
        new_y = el.y + 1
        new_val = mat[new_y][el.x]

        el = HEntry(new_val, el.x, new_y)
        heapq.heappush(heap, el)
    return heap[0].val


if __name__ == '__main__':
    k = int(sys.stdin.readline())
    rows = int(sys.stdin.readline())
    cols = int(sys.stdin.readline())

    matrix = []

    for i in range(rows):
        matrix.append([int(x) for x in sys.stdin.readline().split(" ")])

    el = findKthSmallest(matrix, rows, cols, k)
    print el
