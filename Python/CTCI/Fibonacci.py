memo = {0: 0,
        1: 1}


def fibonacci(n):
    if n in memo:
        return memo[n]

    else:
        num = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n] = num  # Memoize num.

        return num