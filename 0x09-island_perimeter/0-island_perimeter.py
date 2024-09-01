#!/usr/bin/python3
""" Island perimeter algorithm
"""


def island_perimeter(grid):
    """ Function calculates the perimeter of an island

    Args:
        grid(list of lists): rectangular area where perimeter is to be found

    Return:
        int: perimeter of an island inside the grid
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1
    return perimeter
