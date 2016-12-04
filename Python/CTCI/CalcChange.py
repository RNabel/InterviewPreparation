#!/bin/python

import sys

memo = {}


def make_change(coins, n):
    coins.sort()
    return make_change_helper(coins, n, len(coins))


def make_change_helper(coins, n, max_coin_ind):
    if (n, max_coin_ind) in memo:
        return memo[(n, max_coin_ind)]

    # If sum is exactly 0, one solution found.
    if n == 0:
        return 1

    # If sum is negative there's no solution.
    if n < 0:
        return 0

    if n > 0 and max_coin_ind <= 0:
        return 0

    num_solutions = make_change_helper(coins, n, max_coin_ind - 1) + \
                    make_change_helper(coins,
                                       n - coins[max_coin_ind - 1],
                                       max_coin_ind)

    # Memoize the solutions found.
    memo[(n, max_coin_ind)] = num_solutions

    return num_solutions


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
coins = map(int, raw_input().strip().split(' '))
print make_change(coins, n)
