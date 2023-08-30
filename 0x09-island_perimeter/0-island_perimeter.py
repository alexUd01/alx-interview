#!/usr/bin/python3
"""
Create a function `def island_perimeter(grid)`: that returns the perimeter of
the island described in `grid`:

INSTRUCTIONS:
- grid is a list of list of integers:
  - 0 represents water
  - 1 represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the
  water surrounding the island).
"""

def count_surrounding_water(_list):
    """
    A helper function that calculates and returns the unit length of a `1`
    on the `grid`.
    """
    return _list.count(0)

def island_perimeter(grid):
    """ The function """
    if grid is None or type(grid) is not list:
        return 0

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                if i == 0:  # First iteration has no above
                    abv = 0
                else:
                    abv = grid[i - 1][j]
                if i == len(grid) - 1:  # Last iteration has no below
                    bel = 0
                else:
                    bel = grid[i + 1][j]
                if j == 0:  # First iteration of 2nd loop has no left
                    left = 0
                else:
                    left = grid[i][j - 1]
                if j == len(grid[i]) - 1:  # Last iter of 2nd loop has no right
                    rght = 0
                else:
                    rght = grid[i][j + 1]
                perimeter += count_surrounding_water([abv, bel, left, rght])

    return perimeter
