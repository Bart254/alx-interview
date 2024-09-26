#!/usr/bin/python3
"""Data Structure and Algorithm
"""


def island_perimeter(grid):
    """ Returns perimeter of an island
    """
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    # Iterate through each cell in the grid

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Add 4 sides for each land cell initially
                perimeter += 4

                # Check if the adjacent cell above is also land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove 2 sides (shared edge)

                # Check if the adjacent cell to the left is also land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Remove 2 sides (shared edge)
    return perimeter
