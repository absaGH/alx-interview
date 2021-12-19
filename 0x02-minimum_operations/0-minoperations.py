#!/usr/bin/python3
import sys
"""A module to solve minimum operations challenge"""


def minOperations(n):
    """Function implementation of minimum operations finder algorithm"""
    copy = 0
    paste = 0
    ops = 0
    counter = 1

    if n <= 1 or sys.getsizeof(n) > 28:
        return 0

    for i in range(n):
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
