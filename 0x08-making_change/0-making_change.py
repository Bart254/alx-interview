#!/usr/bin/python3
"""Minimum change algorithm
"""


def makeChange(coins, total):
    """returns minimum change of coins required for a total amount of money

    Args:
        coins(list): denominations of coins from which change is acquired
        total(int): value to be obtained from denominations

    Returns:
        minimum number of coins
    """
    if total == 0:
        return -1

    # sort coins in descending order
    coins.sort(reverse=True)

    total_cp = total
    min_coins = 0
    for i in range(len(coins)):
        for j in range(i, len(coins)):
            if coins[j] > total:
                continue
            quotient = total // coins[j]
            remainder = total - (quotient * coins[j])
            min_coins += quotient
            if remainder == 1 and 1 not in coins:
                remainder += coins[j]
                min_coins -= 1
            if remainder == 0:
                return min_coins
            total = remainder
        # reset min_coins and total
        min_coins = 0
        total = total_cp

    return -1
