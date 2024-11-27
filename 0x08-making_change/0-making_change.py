#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    elif len(coins) < 1:
        return -1

    change_amt = 0

    sort_coins = sorted(coins)[::-1]
    for coin in sort_coins:
        while coin <= total:
            total -= coin
            change_amt += 1
        if (total == 0):
            return change_amt

    return -1
