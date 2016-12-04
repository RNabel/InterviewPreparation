import sys


def find_largest_sum_contiguous(arr):
    if len(arr):
        sums = [0] * (len(arr) + 1)
        lengths = [0] * (len(arr) + 1)

        for i in range(len(arr) - 1, -1, -1):
            current_sum = arr[i]
            current_len = 1
            best_from_next_sum = sums[i + 1]
            best_from_next_len = lengths[i + 1]

            if best_from_next_sum > 0:
                current_sum += best_from_next_sum
                current_len += best_from_next_len

            sums[i] = current_sum
            lengths[i] = current_len

        # Find best.
        max_index = sums.index(max(sums[:-1]))
        max_cost = sums[max_index]
        max_length = lengths[max_index]

        return max_index, max_cost, max_length
    else:
        return 0


def find_largest_sum_non_contiguous(arr):
    if len(arr):
        filtered_arr = filter(lambda x: x > 0, arr)
        if len(filtered_arr):
            return reduce(lambda prev, curr: prev + curr, filtered_arr)
        else:  # return largest element
            return max(arr)

    else:
        return 0


if __name__ == '__main__':
    num = int(sys.stdin.readline())
    for i in range(num):
        array_length = int(sys.stdin.readline())
        array = [int(x) for x in sys.stdin.readline().split(" ")]
        cont_res = find_largest_sum_contiguous(array)[1]
        non_cont_res = find_largest_sum_non_contiguous(array)
        print "%d %d" % (cont_res, non_cont_res)
