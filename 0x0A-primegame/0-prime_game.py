#!/usr/bin/python3
"""
Prime Game
"""


def remove_prime_multiples(list_primes, i):
    """
        Remove multiples of prime numbers
    """

    for j in range(2, len(list_primes)):
        try:
            list_primes[j * i] = 0
        except (ValueError, IndexError):
            break


def isWinner(x, nums):
    """
    Find the winner of x rounds of the Prime Game

    Maria and Ben are playing a game.
    Determine who the winner of each game is
    """

    if (x <= 0 or nums is None or x != len(nums)):
        return None

    maria, ben = 0, 0

    choice = [1 for x in range(sorted(nums)[-1] + 1)]
    choice[0], choice[1] = 0, 0

    for a in range(2, len(choice)):
        remove_prime_multiples(choice, a)

    for i in nums:
        if sum(choice[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
