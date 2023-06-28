#!/usr/bin/python3
""" A function def that returns a list of lists of integers representing
the Pascal’s triangle of n: Returns an empty list if n <= 0
"""


def pascal_triangle(n):
    """ The function """

    result = []

    if n <= 0:
        return result

    prev = [1, 1]
    for i in range(n):
        if i == 0:  # 0th Step (static)
            result.append([1])
            continue
        if i == 1:  # 1st Step (static)
            result.append([1, 1])
            continue

        curr = [1]  # Insert the first `1` manually
        for j in range(len(prev) - 1):  # 2nd - nth steps (dynamic)
            curr.append(prev[j] + prev[j + 1])
        curr.append(1)  # Insert the last `1` manually

        result.append(curr)
        prev = curr  # update `prev` to point to the newly created list

    return result
