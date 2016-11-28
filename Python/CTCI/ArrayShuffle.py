def array_left_rotation(a, n, k):
    if a is None or not len(a):  # Catch invalid array.
        return a

    k %= n

    copy = a[:]
    for i in range(n):
        # Replace current element with element at index current + k.
        index = (i + k) % n
        a[i] = copy[index]

    return a


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k)
print ' '.join(map(str, answer))
