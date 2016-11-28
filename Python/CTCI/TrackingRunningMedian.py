import heapq

import sys


class RunningMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.num_of_els = 0

    def add(self, value):

        # First element.
        if not self.num_of_els:
            self.min_heap.append(value)

        else:
            # Add element to correct heap.
            if value > self.min_heap[0]:
                heapq.heappush(self.min_heap, value)
            else:
                heapq.heappush(self.max_heap, -value)

            # Balance heaps.
            len_min = len(self.min_heap)
            len_max = len(self.max_heap)
            if len_max != len_min:
                if len_max > len_min:
                    val = -heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, val)
                else:
                    val = heapq.heappop(self.min_heap)
                    heapq.heappush(self.max_heap, -val)
        self.num_of_els += 1

    def get_median(self):
        if self.num_of_els % 2 == 0:  # If even.
            return round((-self.max_heap[0] + self.min_heap[0]) / 2.0, 1)

        else:  # If odd, return smallest element in min.
            min_size = len(self.min_heap)
            max_size = len(self.max_heap)
            if min_size > max_size:
                return self.min_heap[0]
            else:
                return -self.max_heap[0]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    mean = RunningMedian()

    for i in range(n):
        num = float(sys.stdin.readline().strip())
        mean.add(num)
        print "{0:0.1f}".format(mean.get_median())
