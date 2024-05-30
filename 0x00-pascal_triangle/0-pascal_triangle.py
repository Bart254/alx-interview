#!/usr/bin/python3
""" Pascal Triangle Module
"""


def pascal_triangle(n):
    """ Pascal_triangle function draws a pascal triangle

    Args:
        n(int): number of rows to draw

    Returns:
        list: A list of lists of int of every pascal triangle row
    """
    if n == 0:
        return []

    main = [[1]]
    for row in range(1, n):
        row_list = [1]
        for col in range(1, row):
            value = main[row - 1][col] + main[row - 1][col - 1]
            row_list.append(value)
        row_list.append(1)
        main.append(row_list)
    return main
