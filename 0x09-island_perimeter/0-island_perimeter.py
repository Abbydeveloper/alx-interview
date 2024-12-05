#!/usr/bin/python3
""" Island Perimeter"""


def island_perimeter(grid):
    """A function that returns the perimeter of the island
    described in grid

    Args:
        grid - list of list of integers representing the island
    Return:
        Perimeter of the island
    """

    perimeter = 0;

    for i in range(len(grid)):
        length = 0
        for j in range(len(grid)):
            if grid[i][j] == 0:
                continue
            if i == 0 or grid[i - 1][j] == 0:
                length += 1
            if j == 0 or grid[i][j - 1] == 0:
                length += 1
            if i == len(grid) - 1 or grid[i + 1][j] == 0:
                length += 1
            if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                length += 1

        perimeter += length
    return perimeter
