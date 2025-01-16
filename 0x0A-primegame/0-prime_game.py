#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """
      Check if n is a prime number
    """

    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1.2)) + 1, 2):
            if n % i == 0:
                return False
        return True


def isWinner(x, nums):
    """
    Find the winner of x rounds of the Prime Game

    Maria and Ben are playing a game.
    Determine who the winner of each game is
    """

    # if (x <= 0 or
    #   nums is None or
    #   x != len(nums)):
    #     return None
    # maria, ben = 0, 0

    # choice = [1 for x in range(sorted(nums)[-1] + 1)]
    # choice[0], choice[1] = 0, 0

    # for a in range(2, len(choice)):
    #     try:
    #         choice[a * a] = 0
    #     except (ValueError, IndexError):
    #         break
        
    # for i in nums:
    #     if sum(choice[0:i + 1]) % 2 == 0:
    #         ben += 1
    #     else:
    #         maria += 1

    # if ben > maria:
    #     return "Ben"
    # elif maria > ben:
    #     return "Maria"
    # return None


    def round_winner(n, x):
        """
          Find the winner of each round of the prime game
        """
        choice = [i for i in range(1, n + 1)]

        for i in range(x):
            player = "Ben" if i % 2 == 0 else "Maria"
            prime = -1
            prime_indexes = []

            for i, num in enumerate(choice):
                if prime != -1:
                    if num % prime == 0:
                        prime_indexes.append(i)
                else:
                    if is_prime(num):
                        prime_indexes.append(i)
                        prime = num

            if prime == -1:
                if player == "Maria":
                    return "Ben"
                else:
                    return "Maria"
            else:
                for i, val in enumerate(prime_indexes):
                    del choice[val - i]

        return None
    
    maria = 0
    ben = 0

    for i in range(x):
        winner = round_winner(nums[i], x)
        if winner is not None:
            if winner == "Maria":
                maria += 1
            if winner == "Ben":
                ben += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None