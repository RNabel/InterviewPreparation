def find_largest_sum_contiguous(arr):
    if len(arr):
        sums = [0] * (len(arr) + 1)
        lengths = [0] * (len(arr) + 1)

        for i in range(len(arr) - 1, 0, -1):
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
        max_index = sums.index(max(sums))
        max_cost = sums[max_index]
        max_length = lengths[max_index]

        return max_index, max_cost, max_length
    else:
        return False


def find_largest_sum_non_contiguous(arr):
    if len(arr):
        arr = filter(lambda x: x > 0, arr)
        return reduce(lambda prev, curr: prev + curr, arr, 0)
    else:
        return False


if __name__ == '__main__':
    test_arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    res = find_largest_sum_contiguous(test_arr)
    print res

    res = find_largest_sum_non_contiguous(test_arr)
    print res
