def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = max(excl, incl)

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return max(excl, incl)


arr = [5, 5, 10, 100, 10, 5]
print find_max_sum(arr)

arr = [3, 2, 7, 10]
print find_max_sum(arr)
