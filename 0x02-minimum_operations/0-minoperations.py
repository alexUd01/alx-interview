#!/usr/bin/python3
""" Interview Preparation Question:

QUESTION:
In a text file, there is a single character `H`. Your text editor can execute
only two operations in this file: `Copy All` and `Paste`. Given a number `n`,
write a method that calculates the fewest number of operations needed to
result in exactly n `H` characters in the file.

INSTRUCTION:
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

EXAMPLE:
n = 9
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH =>
    Paste => HHHHHHHHH

Number of operations: 6
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
