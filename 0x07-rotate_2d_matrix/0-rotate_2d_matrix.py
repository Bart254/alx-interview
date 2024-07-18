#!/usr/bin/env python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate matrix 90 degrees clockwise
    """
    n = len(matrix)

    for a in range(n):
        for b in range(a, n):
            matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]

    for a in range(n):
        matrix[a].reverse()
