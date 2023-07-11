#!/usr/bin/python3
""" Don't forget to document later
"""


def minOperations(n):
    """ The function """
    if n == 1:
        return 0

    no_H = 1
    count = 1 # First operation `Copy All` (a must)

    while no_H < n:
        if no_H >= 3:
            if no_H * 2 <= n:
                no_H *= 2
                count += 2  # `Copy` then `Paste` (2 operations)
            else:
                no_H *= 2
                count += 1  # `Paste operation only`
        else:
            no_H += 1
            count += 1

    return count
