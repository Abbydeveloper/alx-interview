#!/usr/bin/python3
"""Rotate a 2d matrix"""

def rotate_2d_matrix(matrix):
    """Rotate a @D matrix,
        90 degrees clockwise

        Args:
            matrix - matrix to rotate
        Returns:
            None
    """
    length = len(matrix)

    for i in range(n / 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j],
            matrix[i][j]

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
