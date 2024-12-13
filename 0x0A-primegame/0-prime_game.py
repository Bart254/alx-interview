#!/usr/bin/python3
def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Step 1: Generate primes up to max_num using Sieve of Eratosthenes
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_num + 1, i):
                primes[multiple] = False

    # Step 2: Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1  # Ben wins if the number of primes is even
        else:
            maria_wins += 1  # Maria wins if the number of primes is odd

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
