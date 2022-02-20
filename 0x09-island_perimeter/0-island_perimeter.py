#!/usr/bin/python3
"""
It create a function def island_perimeter(grid): that returns the perimeter of
the island described in grid
"""


def island_perimeter(grid):
    """
    Implements the function to calculate perimeter of an island
    """
    d = 0
    perm = 0
    width = len(grid)
    length = len(grid[0])
    for line in grid:
        c = 0

        for val in line:
            if val == 1:
                surround = 4
                if c != length - 1:
                    if grid[d][c + 1] == 1:
                        surround -= 1
                if c != 0:
                    if grid[d][c - 1] == 1:
                        surround -= 1
                if d != width - 1:
                    if grid[d + 1][c] == 1:
                        surround -= 1
                if d != 0:
                    if grid[d - 1][c] == 1:
                        surround -= 1
                perm += surround
            c += 1
        d += 1
    return perm
