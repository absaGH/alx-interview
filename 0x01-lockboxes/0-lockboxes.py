#!/usr/bin/python3
"""Python implementation of the Lockboxes challenge"""


def canUnlockAll(boxes):
    """function that returns True if all boxes can be unlocked, false otherwie"""
    size = len(boxes)
    flags = [1]
    for i in range(1, size, 1):
        flags.append(0)
    for j in range(len(boxes)):
        if (flags[j] == 1):
            for k in range(len(boxes[j])):
                if((boxes[j][k] < size) and flags[boxes[j][k]] == 0):
                    flags[boxes[j][k]] = 1
                    if(j > boxes[j][k]):
                        for m in range(len(boxes[boxes[j][k]])):
                            if((boxes[boxes[j][k]][m] < size) and flags[boxes[boxes[j][k]][m]] == 0):
                                flags[boxes[boxes[j][k]][m]] = 1
    if (0 in flags):
        return False
    return True
