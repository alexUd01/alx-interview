#!/usr/bin/python3
"""
QUESTION:
Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.
- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty
"""


def clone_matrix(matrix):
    """ A helper function that clones and returns a list of lists  """
    clone = []
    for row in matrix:
        item = []
        for col in row:
            item.append(col)
        clone.append(item)
    return clone


def rotate_2d_matrix(matrix):
    """ a function that rotates a 2D matrix by 90 degrees """
    n = len(matrix)
    clone = clone_matrix(matrix)

    for row in range(n):
        k = n - 1
        for col in range(n):
            matrix[row][col] = clone[k][row]
            # print('matrix[{}][{}] = clone[{}][{}] (ie. {})'.format(
            # row, col, k, row, clone[k][row]))
            k -= 1
            if k == -1:
                break
