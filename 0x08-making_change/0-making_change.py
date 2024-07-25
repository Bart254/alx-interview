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

    min_coins = 0
    for i in range(len(coins)):
        if coins[i] > total:
            continue
        quotient = total // coins[i]
        remainder = total - (quotient * coins[i])
        min_coins += quotient
        if remainder == 0:
            return min_coins
        total = remainder

    return -1
