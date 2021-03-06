#!/usr/bin/python3
"""A module to solve minimum operations challenge"""


def minOperations(n):
    """Function implementation of minimum operations finder algorithm"""
    copy = 0
    paste = 0
    ops = 0
    counter = 1

    if n <= 1:
        return 0

    while n != counter:
        if counter < n:
            if n % counter == 0:
                copied = counter
                copy = copy + 1
                paste = paste + 1
                counter += copied
            else:
                paste = paste + 1
                counter += copied
        ops = copy + paste
    return ops
