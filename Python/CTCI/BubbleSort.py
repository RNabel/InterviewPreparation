def bubble_sort(nums):
    total_swaps = 0

    for i in range(len(nums)):
        swaps = 0
        for j in range(len(nums) - 1):
            # Swap elements as necessary.
            left = nums[j]
            right = nums[j + 1]
            if left > right:
                nums[j + 1] = left
                nums[j] = right
                swaps += 1

        if not swaps:  # No swaps occurred so can exit.
            break

        total_swaps += swaps

    return nums, total_swaps, nums[0], nums[-1]


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

res = bubble_sort(a)

print "Array is sorted in %d swaps." % res[1]

print "First Element: %d" % res[2]
print "Last Element: %d" % res[3]
