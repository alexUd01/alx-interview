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
    if n <= 1 or type(n) is not int:
        return 0

    ops, root = 0, 2
    while root <= n:
        if n % root == 0:  # if n evenly divides by root
            # total even-divisions by root = total operations
            ops += root
            n = n / root  # set n to the remainder
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        root += 1  # increment root until it evenly-divides n
    return ops
