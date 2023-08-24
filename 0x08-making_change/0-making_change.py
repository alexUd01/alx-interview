#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.

- PROTOTYPE: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`
  - If `total` is 0 or less, return 0
  - If `total` cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in
  the list
- Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """ The function """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
