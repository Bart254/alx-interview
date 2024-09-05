#!/usr/bin/python3
""" Module for determining prime numbers
"""


def isWinner(x, nums):
    """Precompute all prime numbers
    """
    if x == 0 or len(nums) == 0:
        return None
    max_num = max(nums) if x > 0 else 0
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        primes_up_to_n = prime_count[n]

        # Maria wins if the number of primes is odd, Ben wins if it's even
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
