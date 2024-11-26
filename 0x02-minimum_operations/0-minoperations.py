#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """minOperations"""
    """Fewest number of operations needed to get n H characters"""

    if (n < 2):
        return 0

    no_of_operations = 0
    i = 2

    while i <= n:
        if n % i == 0:
            no_of_operations == i
            n = n / i
            i -= 1
        i += 1

    return no_of_operations
