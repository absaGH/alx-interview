#!/usr/bin/python3
"""
A program that generates the Pascal's triangle
"""


def pascal_triangle(n):
    """
    Return  list of lists of integers representing the Pascal’s triangle of n
    """
    pascal = []
    if(n <= 0):
        return pascal
    else:
        for i in range(n):
            pascal.append([])
        for i in range(1, n + 1, 1):
            if(i == 1):
                pascal[i - 1].append(1)
            else:
                for row in range(i):
                    if (row == 0):
                        pascal[i - 1].append(1)
                    elif (row == (i - 1)):
                        pascal[i - 1].append(1)
                    else:
                        pascal[i - 1].append(pascal[i - 2]
                                             [row - 1] + pascal[i - 2][row])
    return pascal
