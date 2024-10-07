#!/usr/bin/python3
"""Return a list of lists of integers representing the Pascal's triangle"""


def pascal_triangle(n):
    """Args:
        n (int): The number of rows of the triangle

    Returns:
        list of lists representing the Pascal's triangle"""

    pascal = []
    if n > 0:
        for i in range(n):
            pascal.append([])
            pascal[i].append(1)
            if (i > 0):
                for j in range(1, i):
                    pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])
                pascal[i].append(1)
    return pascal
